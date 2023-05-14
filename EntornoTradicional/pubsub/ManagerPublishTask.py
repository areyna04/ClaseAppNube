from google.cloud import pubsub_v1




class ManagerPublishTask():
    
    def __init__(self,  project_id , topic_name  ) -> None:

        self.topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id=  project_id,
            topic= topic_name,  
        )

        self.publisher = pubsub_v1.PublisherClient()
        self.project_id = project_id 
        ##self.topic_name = topic_name

    def send_task(  self,  message):
        
        tarea = self.publisher.publish(self.topic_name, data=message.encode("utf-8"))
        resultado =   tarea.result()
        