# main.py

from fastapi import FastAPI, Request
from .routes import router
from .models import Cliente
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Define la URL de la base de datos
DATABASE_URL = "sqlite:///clientes.db"

# Inicializar la base de datos
Cliente.inicializar_base_datos(DATABASE_URL)

# Crea una instancia de FastAPI
app = FastAPI(debug=True)

# Incluir las rutas en la aplicación
app.include_router(router)

# Configurar la ruta para los archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configurar la ubicación de los templates
templates = Jinja2Templates(directory="app/templates")

# Otras importaciones y configuraciones

@app.get("/")
async def index(request: Request):
    with open("app/templates/index.html", "r") as file:
        return templates.TemplateResponse("index.html", {"request": request})