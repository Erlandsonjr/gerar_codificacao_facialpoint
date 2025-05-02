from fastapi import FastAPI, UploadFile, File, Form
import face_recognition
import numpy as np
import cv2
from pymongo import MongoClient

app = FastAPI()

# Configuração do MongoDB
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# Escolher o banco de dados e a coleção
db = client["reconhecimento_facial"]
collection = db["codificacoes"]

@app.post("/reconhecer/")
async def reconhecer(cpf: str = Form(...), file: UploadFile = File(...)):
    """
    Endpoint para verificar se a codificação do rosto enviado corresponde ao CPF fornecido.
    Retorna apenas um booleano em JSON.
    """
    dado = collection.find_one({"cpf": cpf}, {"_id": 0})
    if not dado:
        return False

    codificacao_cpf = dado["codificacao"]

    conteudo = await file.read()
    nparr = np.frombuffer(conteudo, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    rostos = face_recognition.face_locations(img_rgb)
    if not rostos:
        return False

    codificacoes = face_recognition.face_encodings(img_rgb, rostos)

    for codificacao_rosto in codificacoes:
        correspondencia = face_recognition.compare_faces([codificacao_cpf], codificacao_rosto, tolerance=0.5)
        if correspondencia[0]:
            return True

    return False
