# API de la Tienda: CRUD de Categorías

Proyecto de la evidencia GA2-AA3-EV04. API construida con FastAPI que permite
crear, listar, actualizar y eliminar categorías de una tienda.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación y ejecución

1. Clonar el repositorio y entrar en la carpeta:

   ```bash
   cd tienda-api
   ```

2. Crear y activar el entorno virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Iniciar el servidor:

   ```bash
   uvicorn main:app --reload
   ```

5. Abrir la documentación interactiva en: http://127.0.0.1:8000/docs

## Endpoints de categorías

| Método | Ruta | Descripción | Código |
|---|---|---|---|
| GET | /categorias | Listar todas | 200 |
| GET | /categorias/{id} | Obtener una por id | 200 / 404 |
| POST | /categorias | Crear una nueva | 201 / 422 |
| PUT | /categorias/{id} | Actualizar el nombre | 200 / 404 |
| DELETE | /categorias/{id} | Eliminar | 200 / 404 |

## Nota

Los datos se guardan en memoria (una lista de Python), por lo que se reinician
cada vez que se apaga el servidor.

## Autor

Luis Miguel Montalvo, aprendiz ADSO (SENA)

## arquitectura del proyecto
tienda-api/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── capturas/
├── venv/            (existe en tu PC, pero no se sube)
└── routers/
    ├── __init__.py
    ├── productos.py
    └── categorias.py