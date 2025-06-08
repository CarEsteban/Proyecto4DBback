# API REST para Sistema de Laboratorios

API REST desarrollada con FastAPI para gestionar pacientes y laboratorios.

## Estructura del Proyecto

```
proyecto4/
├── ProyectoDBback/         # Backend con FastAPI
│   ├── app/
│   │   ├── routers/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├──requirements.txt
│   └── README.md
│
├── bd/                 # Scripts SQL
│   ├── ddl.sql        # Definición de tablas
│   ├── data.sql       # Datos iniciales
│   ├── functions.sql  # Funciones
│   ├── triggers.sql   # Triggers
│   └── views.sql      # Vistas
│   
└── ProyectoDBfront/        # Frontend (interfaz de usuario)
    └── ... archivos del frontend
```

## Requisitos Previos

- Python 3.8+
- PostgreSQL
- pip

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/CarEsteban/Proyecto4DBback.git
cd Proyecto4DBback
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

a) Ingresar a PostgreSQL como usuario postgres:
```bash
psql -U postgres
```

b) Crear la base de datos y asignar el owner (reemplaza 'usuario' con tu nombre de usuario):
```sql
CREATE DATABASE proyecto4bd WITH OWNER = usuario;
```

c) Salir de psql:
```sql
\q
```

d) Asegurarse que las credenciales en `app/database.py` coincidan con tu configuración:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://usuario:contraseña@localhost/proyecto4bd"
```

5. Crear la carpeta `bd/` con los scripts SQL necesarios:
```bash
mkdir bd
touch bd/ddl.sql bd/data.sql bd/functions.sql bd/triggers.sql bd/views.sql
```

- `ddl.sql`: Define las tablas de pacientes y laboratorios
- `data.sql`: Inserta datos de prueba iniciales
- `functions.sql`: Define funciones SQL personalizadas
- `triggers.sql`: Define triggers para la base de datos
- `views.sql`: Define vistas para consultas frecuentes

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