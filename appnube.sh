#!/bin/bash
​
cd /root
# Verificar si Python está instalado y, si no, instalarlo
if ! command -v python &> /dev/null; then
    sudo apt-get update
    sudo apt-get install python -y
fi
​
# Verificar si pip está instalado y, si no, instalarlo
if ! command -v pip &> /dev/null; then
    sudo apt-get install python-pip -y
fi
​
# Verificar si git está instalado y, si no, instalarlo
if ! command -v git &> /dev/null; then
    sudo apt-get install git -y
fi
​
# Verificar si la carpeta existe y eliminarla si es necesario para traer version actual
if [ -d "repositorio" ]; then
    rm -rf ClaseAppNube
fi
​
# Clonar el repositorio de GitHub
git clone https://github.com/areyna04/ClaseAppNube
​
# Moverse al directorio del repositorio
cd ClaseAppNube
​
# Instalar los requisitos de Python
pip install -r requirements.txt
​
# Levantar la aplicación de Flask
export FLASK_APP=app.py
flask run