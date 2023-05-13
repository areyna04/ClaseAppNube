from google.cloud import pubsub_v1
import concurrent.futures

from worker.WorkerCompresion import TareaCompresion

class ManagerSubscriberTask():
    
    def __init__(self) -> None:
        self.subscriber = pubsub_v1.SubscriberClient()


    def suscribir_topic_comprimir(self, project_id, topic_name):
        # Formatear el nombre completo del tema
        subscription_path = self.subscriber.subscription_path(project_id, f"{topic_name}-sub")

        def comprimir_callback (mensaje):
            tarea =  TareaCompresion()
            id_request = mensaje.data.decode('utf-8')
            resultado_ok= tarea.comprimir(id_request)
            if resultado_ok :
                mensaje.ack()

             


        # Iniciar la suscripción
        streaming_pull_future = self.subscriber.subscribe(subscription_path, callback=comprimir_callback)

        # Mantener el proceso en ejecución mientras espera mensajes
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(streaming_pull_future.result)    


