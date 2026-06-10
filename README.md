# FacialPoint — Serviço de Codificação Facial

Microserviço responsável por gerar a codificação facial de um usuário a partir de uma foto, utilizada durante o cadastro no sistema.

## Sobre o projeto

O FacialPoint é um sistema de registro de ponto por reconhecimento facial. Este serviço recebe uma imagem de rosto e retorna um vetor de 128 dimensões que representa matematicamente as características faciais do usuário. Essa codificação é armazenada no banco de dados e usada posteriormente para identificação.

## Tecnologias

- **Python 3.10**
- **FastAPI** — framework web assíncrono
- **face_recognition** — extração de características faciais baseada em dlib
- **OpenCV** — leitura e pré-processamento de imagens
- **NumPy** — operações vetoriais
- **Docker** — containerização

## Funcionalidades

- Recebe uma imagem via upload
- Detecta o rosto presente na imagem
- Gera e retorna a codificação facial (array de 128 floats)
- Retorna erro descritivo caso nenhum rosto seja detectado

## Como executar

**Localmente**
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

**Com Docker**
```bash
docker build -t facialpoint-codificacao .
docker run -p 8000:8000 facialpoint-codificacao
```

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/gerar-codificacao/` | Recebe imagem e retorna vetor de codificação facial |

## Repositórios relacionados

- [FacialPoint-Site](https://github.com/Erlandsonjr/FacialPoint-Site) — Interface web (React)
- [FacialPoint-Banco-Dados](https://github.com/Erlandsonjr/FacialPoint-Banco-Dados) — API backend (Node.js)
- [FacialPoint-Reconhecimento-Facial](https://github.com/Erlandsonjr/FacialPoint-Reconhecimento-Facial) — Serviço de reconhecimento facial (Python)
