Para activar Virtual Enviroment e instalar librerias.

py -m venv env
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
.\env\Scripts\activate
pip install -r .\requirements.txt
pip install --upgrade pip wheel setuptools requests
