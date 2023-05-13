from pubsub.ManagerSubscriberTask import ManagerSubscriberTask  
import os


project_id =  os.getenv('GOOGLE_CLOUD_PROJECT')  
topic_name =  os.environ.get("TOPIC")

managerSub = ManagerSubscriberTask()

managerSub.suscribir_topic_comprimir(project_id,  topic_name)