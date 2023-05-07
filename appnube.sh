#!/bin/bash
​
cd /root

# Moverse al directorio del repositorio
cd ClaseAppNube
​
# Levantar la aplicación de Flask
export FLASK_APP=app.py
export  SQLALCHEMY_DATABASE_URI="postgresql://postgres:convert@35.239.90.117:5432/appnube"
export REDIS_URL="redis://10.128.0.5:6379/0"
export bucket_files="web_api_data"
flask run