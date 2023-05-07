from storage.storageAbstract import IStorage
import uuid
import os 
import base64

class ManagerFiles ():
    def __init__(self ,  storage : IStorage  ) -> None:
        self.storage = storage
        
    def sync(self,  aux_path , file_name  , file_base64  ) :
        try: 
            local_path =os.path.abspath( f"EntornoTradicional/files/{str(uuid.uuid4())}/{file_name}")
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
                
            return  True ,  remote_path , "" 
        except Exception as ext:    
            error =f"Unexpected {ext=}, {type(ext)=}"    
            print(error)
            return False ,  "", error
       
        
    def get_file( self , remote_path   ): 
        try:
            file_name = os.path.basename(remote_path)
            if self.storage   is not None: 
                local_path =   os.path.abspath( f"files/{str(uuid.uuid4())}/{file_name}")
                print(local_path)
                local_dir = os.path.dirname(local_path)
                os.makedirs(local_dir, exist_ok=True)   
                self.storage.get_file( local_path , remote_path)
            else:
                local_path = remote_path 
            if os.path.exists(local_path):
                return True ,   local_path ,  ""
            else :
                return False  , "" , "No existe archivo" 
        except Exception as ext:    
            error =f"Unexpected {ext=}, {type(ext)=}"    
            print(error)
            return False , "" ,  error          
        
    def get_file_base64(self, file_name):
        with open(file_name, 'rb') as file:
            content = file.read()
            return base64.b64encode(content)
    
    def delete_local_file(self ,  local_path_file ):
        try:     
            local_dir = os.path.dirname(local_path_file)
            os.remove(local_path_file)
            os.removedirs(local_dir)
            return True ,  ""
        except Exception as ext:    
            error =f"Unexpected {ext=}, {type(ext)=}"    
            print(error)
            return False ,  error
    
    def delete_remote_file( self , remote_path   ): 
        try:
            return  self.storage.delete_file( remote_path),  ""
            
        except Exception as ext:    
            error =f"Unexpected {ext=}, {type(ext)=}"    
            print(error)
            return False ,  error          