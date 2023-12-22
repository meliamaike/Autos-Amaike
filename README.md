# Desafío Auto 

Este es un proyecto Django que incluye las instrucciones necesarias para levantarlo localmente.

## Requisitos Previos

Asegúrate de tener instalados los siguientes componentes antes de comenzar:

- Python (3.x recomendado)
- Pip (el gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

## Configuración del Entorno Virtual (Opcional)

1. Abrí la terminal en la raíz del proyecto.
2. Crea un entorno virtual:

    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Windows:

        ```bash
        venv\Scripts\activate
        ```

    - En macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

## Instalación de Dependencias

1. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración de la Base de Datos

1. Crea las nuevas migraciones:

    ```bash
    python manage.py makemigrations
    ```

2. Aplica las migraciones para actualizar la base de datos:

    ```bash
    python manage.py migrate
    ```

3. Opcionalmente, crea un superusuario:

    ```bash
    python manage.py createsuperuser
    ```


## Ejecutar el Servidor de Desarrollo

1. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

2. Abre tu navegador y dirigite [http://localhost:8000](http://localhost:8000)

3. Accede al panel de administración con las credenciales del superusuario [http://localhost:8000/admin](http://localhost:8000/admin)

## Detener el Servidor de Desarrollo

Para detener el servidor de desarrollo, presionar `Ctrl + C` en la terminal.

