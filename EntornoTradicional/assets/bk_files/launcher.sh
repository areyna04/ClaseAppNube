#! /bin/bash

# Subir microservicios- Containers api - redis - worker - db postgresql

# Sube Database postgree
sudo docker run --name convert-db -p 5432:5432 -e POSTGRES_PASSWORD=convert -d -v $(pwd)/../db-postgres:/var/lib/postgresql/data postgres

# Run container base de datos -- Redis  -- Conversion tool app

sudo docker run --name redis -d redis


# Create image app Convert Flask-- celery worker

sudo docker build -t api-worker:1.0 .

# Run container -- Flask -- convert tool app
sudo docker run --name api-rest -d -v $(pwd)/../dockervolume:/app/assets api-worker:1.0

# Run container -- Worker Celery -- convert tool app

sudo docker run --name worker-celery -d -v $(pwd)/../dockervolume:/app/assets api-worker:1.0