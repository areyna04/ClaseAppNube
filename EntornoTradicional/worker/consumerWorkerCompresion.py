from celery import Celery

app = Celery( 'tasks-compress' , broker = 'redis://localhost:6379/0' ) 

def sumar_numeros(id_request ):
    print ("-> Se generó una tarea [{}]: {} + {}".format(datetime.now(), x, y))
    return x + y