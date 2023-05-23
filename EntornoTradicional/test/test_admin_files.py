import unittest
from  storage.cloudStorage import CloudStorage
from  admin_files.ManagerFiles import ManagerFiles
import os 


class StorageTestcase(unittest.TestCase ):
    
    def setUp(self) -> None:
        os.environ["bucket_files"] = "bucket-project-cloud-storage-files"
        self.storage = CloudStorage()
        self.manager_files = ManagerFiles(self.storage)
    
    
    def  test_sync_file_sucess( self):
        
        file_base_64  = self.manager_files.get_file_base64( os.path.abspath("test/files/pruebas_upload_from_files_p2.txt"))
        proceso_ok ,  remote_path , mensaje  = self.manager_files.sync( aux_path =  "files/1/10"   , file_name=  "pruebas_upload_from_files_p2.txt" , file_base64 = file_base_64)
        print( remote_path , mensaje )
        self.assertTrue(proceso_ok)    
    
    
    
    
    def  test_get_file_sucess( self):
        
        
        proceso_ok ,  local_path , mensaje  = self.manager_files.get_file("files/1/10/pruebas_upload_from_files_p2.txt")
        print( proceso_ok , local_path )
        existe_file = os.path.exists(local_path)
        self.manager_files.delete_local_file(local_path)
        self.assertTrue(proceso_ok and existe_file)    
    