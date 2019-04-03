# Flask app: TP Arquitectura de Software

## Instalación

* Instalar python 3.7
* Instalar [pipenv](https://pipenv.readthedocs.io/en/latest/install/)
* Instalar dependencias: `pipenv install`

# Levantar server

* En [PyCharm](https://www.jetbrains.com/toolbox/):
    * Run > Edit Configurations > Add New Configuration > Python`
    * Script Path: se obtiene ejecutando `echo $(pipenv --venv)/bin/gunicorn`
    * Parameters: `-w 1 app:app -b 0.0.0.0:8000`

* En consola:
    * `pipenv run gunicorn -w 1 app:app -b 0.0.0.0:8000`
