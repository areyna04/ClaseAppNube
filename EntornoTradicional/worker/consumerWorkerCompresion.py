from celery import Celery

app = Celery( 'tasks-compress' , broker = 'redis://localhost:6379/0' ) 

def comprimir_archivo(id_request ):
    
    
    
    
    return x + y