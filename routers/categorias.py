# Antes (incorrecto): form fastapi import APIRouter, HTTPException
# Ahora (correcto): "from" va primero, así se importa algo de un paquete
from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router = APIRouter(prefix="/categorias", tags=["categorias"])

class CategoriaEntrada(BaseModel):
    nombre:str

categorias =[ 
    {"id":1, "nombre": "perifericos"},
    {"id":2, "nombre": "pantallas"},
    {"id":3, "nombre": "audio"},
]

#esto es lo que responde cuando alguien hace Get a categorias 
@router.get("")
def listar_categorias():
    return categorias


#obtener una categoria por id
@router.get("/{categoria_id}")
def obtener_categoria(categoria_id:int):
    for categoria in categorias:
        if categoria["id"] ==categoria_id:
            return categoria
    raise HTTPException(status_code=404, detail="Categoria no encontrada")


#crear nueva categoria
# CREATE - Crear una nueva categoría
@router.post("", status_code=201)
def crear_categoria(datos: CategoriaEntrada):
    # Las 4 líneas de abajo deben tener EXACTAMENTE 4 espacios al inicio
    nuevo_id = max((c["id"] for c in categorias), default=0) + 1
    nueva = {"id": nuevo_id, "nombre": datos.nombre}
    categorias.append(nueva)
    return {"mensaje": "Categoría creada", "categoria": nueva}

#UPDATE cambiar el nombre de una categoria existente
@router.put("/{categoria_id}")
def actualizar_categoria(categoria_id:int, datos:CategoriaEntrada):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            categoria["nombre"] = datos.nombre # esto modifica el nombre de la categoria
            return {"mensaje": "Categoría actualizada", "categoria": categoria}
    raise HTTPException(status_code=404, detail="Categoria no encontrada")

#DELETE eliminar una categoria existente
@router.delete("/{categoria_id}")
def eliminar_categoria(categoria_id:int):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            categorias.remove(categoria)
            return {"mensaje": "Categoría eliminada"}
    raise HTTPException(status_code=404, detail="Categoria no encontrada")


