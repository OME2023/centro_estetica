from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .models import Cliente
from fastapi.responses import HTMLResponse

router = APIRouter()

class ClienteIn(BaseModel):
    dni: str
    nombre_apellido: str
    edad: int
    antecedentes_personales: str
    antecedentes_hereditarios: str
    alergia: str
    medicacion: str

@router.get("/", response_class=HTMLResponse)
async def read_root():
    with open("app/templates/index.html", "r") as file:
        return file.read()

@router.get("/clientes")
def obtener_clientes():
    return Cliente.obtener_todos()

@router.post("/clientes")
def crear_cliente(cliente: ClienteIn):
    if Cliente.crear(cliente):
        return {"mensaje": "Cliente agregado exitosamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al agregar cliente")
