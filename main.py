
from fastapi import FastAPI

from routers import productos, categorias


app = FastAPI(title="API de la Tienda")


app.include_router(productos.router)
app.include_router(categorias.router)

# Ruta de inicio: responde cuando alguien entra a http://127.0.0.1:8000/
@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "API de la Tienda funcionando. Visita /docs"}