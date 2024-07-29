# ITSA BACKEND

# Pasos de instalación

##### 1) Descomprimir el proyecto en una carpeta de tu sistema operativo

##### 2) Crear un entorno virtual para posteriormente instalar las librerias del proyecto

Para windows:

```bash
python -m venv venv 
```

Para linux:

```bash
virtualenv venv -ppython3 
```

##### 3) Activar el entorno virtual de nuestro proyecto

Para windows:

```bash
venv\Scripts\activate.bat 
```

Para Linux:

```bash
source venv/bin/active
```

##### 4) Instalar todas las librerias del proyecto que se encuentran en la carpeta deploy

```bash
pip install -r deploy/requirements.txt
```

##### 5) Crear la tablas de la base de datos a partir de las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

##### 6) Crear el usuario admin del sitio

```bash
python manage.py start_installation
```

##### 7) Iniciar el servidor del proyecto

```bash
python manage.py runserver 
```
##### 8) Credenciales user: admin

```bash
username: admin
password: 1st44dm1n2024*+
```