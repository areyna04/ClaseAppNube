
from celery import Celery
from worker.WorkerCompresion import TareaCompresion
import os

cnstringRedis =      os.environ.get("REDIS_URL") # "redis://localhost:6379/0" # os.environ["REDIS_URL"]
app = Celery( 'tasks' , broker = cnstringRedis )

@app.task
def comprimir(id_request):
      tarea =  TareaCompresion()
      tarea.comprimir(id_request)