from EntornoTradicional.storage.storageAbstract import IStorage
import uuid
import os 
import base64

class GestorArchivos ():
    def __init__(self ,  storage : IStorage  ) -> None:
        self.storage = storage
        
    def sync(self,  aux_path , file_name  , file_base64  ) :
        try: 
            local_path =   f"{str(uuid.uuid4())}/{aux_path}/{file_name}"
            remote_path =  f"{aux_path}/{file_name}" 
            local_dir = os.path.dirname(local_path)
            os.makedirs(local_dir, exist_ok=True)    
            with open(local_path, "wb") as fh:
                fh.write(base64.b64decode(file_base64))
            if self.storage   is not None:
                self.storage.push_file(local_path , remote_path)
                os.remove(local_path)
                os.removedirs(local_dir)
            else:
                remote_path =   local_path  
                
            return  True ,  "" ,  remote_path
        except Exception as ext:    
            error =f"Unexpected {ext=}, {type(ext)=}"    
            print(error)
            return False , error , ""