# calculadora_ue

Calculadora de escritorio con login/registro, hecha para la asignatura
de Uniempresarial. Python 3.10+ con Tkinter y MySQL local.

## Autores
Tomas Amaya y David Gaitan.

## Stack
- Python 3.10+
- Tkinter (stdlib) para la UI
- MySQL via `mysql-connector-python`
- Pillow para el logo
- python-dotenv para credenciales

## Setup

### 1. Requisitos
- Python 3.10 o superior.
- Un servidor MySQL local (por defecto se asume `localhost:3306`,
  usuario `root` y password vacio, pero se puede cambiar via `.env`).

### 2. Instalar dependencias
```powershell
pip install -r ProyectoFinal/requirements.txt
```

Para correr los tests ademas:
```powershell
pip install -r ProyectoFinal/requirements-dev.txt
```

### 3. Configurar el .env
Copia el template y completa los valores de tu MySQL local:
```powershell
Copy-Item ProyectoFinal\.env.example ProyectoFinal\.env
# edita ProyectoFinal\.env con tus credenciales reales
```

Variables aceptadas:

| Variable          | Default         | Descripcion                              |
|-------------------|-----------------|------------------------------------------|
| MYSQL_HOST        | localhost       | Host del servidor MySQL                  |
| MYSQL_USER        | root            | Usuario de MySQL                         |
| MYSQL_PASSWORD    | (vacio)         | Password del usuario                     |
| MYSQL_PORT        | 3306            | Puerto del servidor MySQL                |
| MYSQL_DATABASE    | sistema_login   | Nombre de la base de datos (se crea sola)|

> La base de datos y la tabla `usuarios` **se crean automaticamente**
> al arrancar la app la primera vez. No hace falta correr scripts SQL
> manuales.

### 4. Correr la app
Desde la raiz del repo:
```powershell
cd ProyectoFinal
python main.py
```

## Tests
```powershell
cd ProyectoFinal
pytest tests/ -v
```
Con cobertura:
```powershell
pytest tests/ -v --cov=. --cov-report=term-missing
```

Los tests mockean la conexion a MySQL, asi que **no** necesitan un
servidor real para correrse.

## Estructura
```
calculadora_ue/
├── .gitignore
├── README.md
└── ProyectoFinal/
    ├── .env.example          # template, commiteado
    ├── .env                  # credenciales reales, NO commiteado
    ├── main.py               # entry point
    ├── login_window.py       # LoginWindow (root Tk)
    ├── register_window.py    # RegisterWindow (Toplevel modal)
    ├── home_window.py        # HomeWindow: grid 2x2 de operaciones
    ├── operacion_window.py   # builder generico de ventana de operacion
    ├── suma.py               # suma.ejecutar(e1, e2, lbl)
    ├── resta.py
    ├── multiplicacion.py
    ├── division.py           # incluye guard de division por cero
    ├── limpiar.py            # limpia campos y resultado
    ├── estilos.py            # design system dark + helpers UI
    ├── database.py           # conexion MySQL + creacion de BD y tabla
    ├── user_repository.py    # registrar_usuario / validar_usuario
    ├── requirements.txt      # deps runtime
    ├── requirements-dev.txt  # deps de testing
    ├── assets/
    │   └── logo.png
    └── tests/
        ├── conftest.py
        ├── test_suma.py
        ├── test_resta.py
        ├── test_multiplicacion.py
        ├── test_division.py
        ├── test_limpiar.py
        ├── test_database.py
        ├── test_user_repository.py
        └── test_login_flujo.py
```