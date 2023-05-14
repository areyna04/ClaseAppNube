from google.cloud import pubsub_v1
import concurrent.futures

from worker.WorkerCompresion import TareaCompresion

class ManagerSubscriberTask():
    
    def __init__(self, project_id, topic_name) -> None:
        self.subscriber = pubsub_v1.SubscriberClient()



        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id=project_id ,
            topic=topic_name,  # Set this to something appropriate.
        )

        subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
            project_id=project_id,
            sub=f"{topic_name}-sub",  # Set this to something appropriate.
        )


        self.subscription_path =  subscription_name  # self.subscriber.subscription_path(project_id, f"{topic_name}-sub")
        self.subscriber.create_subscription(name=self.subscription_path, topic=topic_name)
        print(f'subscripcion  path {self.subscription_path}  topico : {topic_name} ' )

    def suscribir_topic_comprimir(self):
        # Formatear el nombre completo del tema
        try:

            def comprimir_callback (mensaje):    
                tarea =  TareaCompresion()
                id_request = mensaje.data.decode('utf-8')
                print(f'procesando mensaje   {id_request} ' )
                resultado_ok= tarea.comprimir(id_request)
                if resultado_ok :
                    mensaje.ack()

                
            # Iniciar la suscripción
            streaming_pull_future = self.subscriber.subscribe(self.subscription_path, callback=comprimir_callback)
            print(f'suscrito a subscripcion     {self.subscription_path} ' )

            # Mantener el proceso en ejecución mientras espera mensajes
            with concurrent.futures.ThreadPoolExecutor() as executor:
                print(f'corriendo worker')
                executor.submit(streaming_pull_future.result)    
        except KeyboardInterrupt:
            streaming_pull_future.cancel()

