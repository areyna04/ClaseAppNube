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
     
        
    
    def push_file(self ,  file_name_local ,file_name_remote   ) -> bool:
        try:
            blob = self.bucket.blob(file_name_remote)
            blob.upload_from_filename(file_name_local)
            return True 
        except Exception as ext:    
                error =f"Unexpected {ext=}, {type(ext)=}"    
                print(error)
                return False      

        
        
    def get_file(self ,file_name_local ,file_name_remote    ):
        try:
            blob = self.bucket.blob(file_name_remote)
            if  blob.exists():
                blob.download_to_filename(file_name_local)
                return True
            else:
                return False
        except Exception as ext:    
            error =f"Unexpected {ext=}, {type(ext)=}"    
            print(error)
        
        return False     
        
    def delete_file(self , file_name_remote    ):
        try:
            blob = self.bucket.blob(file_name_remote)
            if blob.exists():
                blob.delete()
            return True
        except Exception as ext:    
            error =f"Unexpected {ext=}, {type(ext)=}"    
            print(error)
        return False     
    
    def exists_file(self , file_name_remote    ):
        try:
            blob = self.bucket.blob(file_name_remote)
            return blob.exists()
            
        except Exception as ext:    
            error =f"Unexpected {ext=}, {type(ext)=}"    
            print(error)        
        return False       