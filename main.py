from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

# Armazena na memória
usuarios = {}


class Usuario(BaseModel):
    cpf: int
    nome: str
    data_nascimento: date


@app.post("/usuario/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    if usuario.cpf in usuarios:
        raise HTTPException(status_code=400, detail="Usuário com esse CPF já existe.")

    usuarios[usuario.cpf] = usuario
    return usuario


@app.get("/usuario/{cpf}", response_model=Usuario)
def obter_usuario(cpf: int):
    usuario = usuarios.get(cpf)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    return usuario


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

