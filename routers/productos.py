from fastapi import APIRouter

router = APIRouter(prefix="/productos", tags=["productos"])

@router.get("")
def listar_productos():
    return [{"id":1, "nombre": "teclado"}]