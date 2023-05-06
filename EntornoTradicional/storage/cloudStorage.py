from  google.cloud import storage 
import os 
from storage.storageAbstract import IStorage 

class CloudStorage (IStorage):
    
    def __init__(self) -> None:
        super().__init__()
        #"bucket-project-cloud-storage-files"
        name_bucket = os.environ.get("bucket_files");
        self.client = storage.Client()
        self.bucket  = self.client.bucket(name_bucket)  
        
    
    def push_file(self ,  fileNameLocal,fileNameRemote   ):
        blob = self.bucket.blob(fileNameRemote)
        blob.upload_from_file(fileNameLocal)
        
    def get_file(self ,fileNameLocal,fileNameRemote   ):
        blob = self.bucket.blob(fileNameRemote)
        blob.download_to_filename(fileNameLocal)
        