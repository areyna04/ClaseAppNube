from  google.cloud import storage 

from storage.storageAbstract import IStorage 

class CloudStorage (IStorage):
    
    def __init__(self) -> None:
        super().__init__()
        self.client = storage.Client()
        self.bucket  = self.client.bucket("bucket-project-cloud-storage-files")  
        
    
    def push_file(self ,  file  ,  filename):
        blob = self.bucket.blob(filename)
        blob.upload_from_file(file)
        
    def get_file(self , file ,  filename):
        blob = self.bucket.blob(filename)
        blob.download_to_file(file)
        return file