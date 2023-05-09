## 1.-Verifico la versión de Python

    python --version
    py --version

    Python 3.10.11

## 2.-Actualizo pip

**pip** es un administrador de paquetes para Python. Los paquetes son módulos de código que se pueden usar en Python. Los paquetes son geniales porque pueden ser compartidos con otros o reutilizados en otros proyectos. Puede instalar paquetes usando pip.

    python -m pip install --upgrade pip
## 2.1.-Verifico la versión de pip

    pip --version

    pip 23.1.2 from C:\Users\fernando\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

## 3.-Creo el entorno virtual con venv

 El módulo **venv** está incluido en la biblioteca estándar de Python, lo que significa que viene preinstalado con cualquier instalación de Python. Por lo tanto, no necesita instalar nada adicionalmente para utilizar el módulo venv. Puede utilizarlo directamente en su código Python o desde la línea de comandos.

 En mi notebook tengo instaladas las versiones de Python 3.10.11 y 3.8.8, por lo que puedo crear el entorno virtual con cualquiera de las dos versiones.

    C:\Users\fernando\AppData\Local\Programs\Python

Despues de instalar las versiones de Python en Windows, se crean las carpetas `Python310` y `Python38` en la ruta `C:\Users\fernando\AppData\Local\Programs\Python`.  

**IMPORTANTE**: Tengo que verificar las rutas de las variables de usuario `PATH` y de las variables de sistema `Path` para que apunten a la versión de Python que quiero utilizar.

    python -m venv venv
    py -m venv venv

Para crear el entorno con la version que quiero utilizar, ejecuto el siguiente comando:

    C:\Users\fernando\AppData\Local\Programs\Python\Python310\python.exe -m venv venv-3.10.11

    

## 4.-Activo el entorno virtual (venv)

    venv\Scripts\activate

Para activar un entorno especifico

    venv-3.10.11\Scripts\activate

## 4.1-Comandos para instalar y desinstalar paquetes

    pip install
    pip uninstall

## 5.-Instalo Django

Instalar Django después de activar el entorno virtual (venv), ya que de esta manera puede asegurarse de que se instale dentro del entorno virtual y no afecte a otros proyectos o a la instalación global de Python.

Después de activar el entorno virtual `venv`, puedes instalar Django utilizando `pip`. A continuación, se muestra el comando para instalar Django:

```bash
pip install django
```

Este comando instalará la última versión de Django en tu entorno virtual activo. Si deseas instalar una versión específica de Django, puedes especificar la versión junto con el nombre del paquete. Por ejemplo, para instalar Django 3.2, ejecuta:

```bash
pip install django==3.2
```

Una vez que Django esté instalado, podrás verificar la instalación y la versión ejecutando este comando:

```bash
python -m django --version
```

Esto mostrará la versión de Django instalada en tu entorno virtual activo [Source 2](https://roylans.dev/creando-un-entorno-virtual-para-django-framework).

## 5.1.-Comando pip list

    pip list

    Package    Version
    ---------- -------
    asgiref    3.6.0
    Django     4.2.1
    pip        23.1.2
    setuptools 65.5.0
    sqlparse   0.4.4
    tzdata     2023.3

**pip list** es un comando que muestra la lista de paquetes instalados en el entorno virtual activo. Este comando es útil para verificar qué paquetes están instalados en tu entorno de desarrollo, lo que te permite identificar posibles dependencias faltantes o innecesarias.

## 6.-Ejecutar pip freeze > requirements.txt

El comando pip freeze > requirements.txt se utiliza para guardar las dependencias de tu proyecto en un archivo llamado requirements.txt. Es una buena práctica ejecutar este comando después de instalar todas las dependencias iniciales de tu proyecto y cada vez que agregues, actualices o elimines una dependencia.

    pip freeze > requirements.txt

Se crea el archivo `requirements.txt` con las dependencias del proyecto.

    asgiref==3.6.0
    Django==4.2.1
    sqlparse==0.4.4
    tzdata==2023.3

## 7.-Crear un proyecto Django

    django-admin startproject core .

Me crea la carpeta `core` con los archivos necesarios para iniciar el proyecto, y la estructura de carpetas y archivos es la siguiente:

    manage.py
    core
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py

## 8.-Ejecutar el servidor de desarrollo

    py manage.py runserver

Para cerrar el servidor de desarrollo, presiona

    ctrl + c

## 9.-Crear una aplicación

    py manage.py startapp newapp

Me crea la carpeta `newapp` con los archivos necesarios para iniciar la aplicación, y la estructura de carpetas y archivos es la siguiente:

    newapp
    migrations
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py

## 11.-Registrar la aplicación creada 'newapp' en el archivo settings.py de la carpeta core (13)

```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'newapp', # Registrar la aplicación creada
    ]
```	

## 12.-Crear una vista