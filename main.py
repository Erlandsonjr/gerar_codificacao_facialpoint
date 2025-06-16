from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import face_recognition
import numpy as np
import cv2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/gerar-codificacao/")
async def gerar_codificacao(file: UploadFile = File(...)):
    """
    Endpoint para receber uma imagem, gerar a codificação facial e retornar a codificação.
    """
    conteudo = await file.read()
    nparr = np.frombuffer(conteudo, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    rostos = face_recognition.face_locations(img_rgb)
    if not rostos:
        return JSONResponse(status_code=400, content={"detail": "Nenhum rosto detectado na imagem."})

    codificacoes = face_recognition.face_encodings(img_rgb, rostos)
    if not codificacoes:
        return JSONResponse(status_code=400, content={"detail": "Não foi possível gerar codificação facial."})

    return codificacoes[0].tolist()
