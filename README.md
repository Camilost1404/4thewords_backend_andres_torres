# 4TheWords - Prueba Backend

Backend del proyecto **4TheWords Prueba**, desarrollado con **FastAPI**.

## 📌 Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.8+**
- **Poetry** (para la gestión de dependencias)
- **FastAPI** (framework principal)
- **Alembic** (para migraciones de base de datos)

## 🚀 Instalación

Sigue estos pasos para configurar el proyecto en tu entorno:

1. **Clonar el repositorio**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. **Navegar al directorio del proyecto**

   ```bash
   cd "D:/Proyectos Web/4TheWords Prueba/backend"
   ```

3. **Instalar las dependencias con Poetry**

   ```bash
   poetry install
   ```

## ⚙️ Configuración

1. Crea un archivo `.env` en el directorio raíz del proyecto y define las siguientes variables de entorno:

   ```ini
   ENV="local"
   APP_NAME="4TheWords Test"

   # Configuración de la Base de Datos
    DATABASE_URL="mysql://usuario:contraseña@localhost:3306/4thewords_db"
   ```

## ▶️ Uso

1. Inicia una nueva shell de Poetry:

    ```bash
    poetry shell
    ```

2. Usa el script SQL para crear la base de datos.

3. Aplica las migraciones de la base de datos:

    ```bash
    alembic upgrade head
    ```

4. Usa el script SQL para sembrar datos en la base de datos.

5. Inicia el servidor de desarrollo:

    ```bash
    poetry run uvicorn main:app --reload
    ```

6. Accede a la API en `http://localhost:8000`.

7. La documentación interactiva de la API está disponible en:

    - **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
    - **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📦 Migraciones de Base de Datos

Para gestionar las migraciones de la base de datos con **Alembic**, usa los siguientes comandos:

1. **Crear una nueva migración:**

   ```bash
   alembic revision --autogenerate -m "Descripción de la migración"
   ```

2. **Aplicar las migraciones:**

   ```bash
   alembic upgrade head
   ```


## 📜 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más información.