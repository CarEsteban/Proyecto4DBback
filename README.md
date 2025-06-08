# API REST para Sistema de Laboratorios

API REST desarrollada con FastAPI para gestionar pacientes y laboratorios.

## Requisitos Previos

- Python 3.8+
- PostgreSQL
- pip

## Instalación

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd ProyectoDBback
```

2. Crear un entorno virtual e instalarlo:

```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
.\venv\Scripts\activate  # En Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar la base de datos:

- Crear una base de datos PostgreSQL llamada `proyecto4bd`
- Asegurarse que las credenciales en `app/database.py` coincidan con tu configuración:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://usuario:contraseña@localhost/proyecto4bd"
```

## Estructura de Archivos SQL

Crear una carpeta `bd/` en la raíz del proyecto con los siguientes archivos:
- `ddl.sql`: Definición de tablas
- `data.sql`: Datos iniciales
- `functions.sql`: Funciones SQL
- `triggers.sql`: Triggers
- `views.sql`: Vistas

## Ejecución

1. Iniciar el servidor de desarrollo:

```bash
uvicorn app.main:app --reload
```

2. Visitar la documentación interactiva:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints Disponibles

### Pacientes
- `GET /pacientes/`: Lista todos los pacientes
- `POST /pacientes/`: Crea un nuevo paciente
- `GET /pacientes/{id}`: Obtiene un paciente por ID
- `PUT /pacientes/{id}`: Actualiza un paciente
- `DELETE /pacientes/{id}`: Elimina un paciente
- `GET /pacientes/recientes`: Lista pacientes recientes

### Laboratorios
- `GET /laboratorios/`: Lista todos los laboratorios
- `POST /laboratorios/`: Crea un nuevo laboratorio
- `GET /laboratorios/{id}`: Obtiene un laboratorio por ID
- `PUT /laboratorios/{id}`: Actualiza un laboratorio
- `DELETE /laboratorios/{id}`: Elimina un laboratorio
- `GET /laboratorios/recientes`: Lista laboratorios recientes