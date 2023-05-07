import unittest
import os 
from EntornoTradicional.storage.cloudStorage import CloudStorage

class StorageTestcase(unittest.TestCase ):
    
    
    def setUp(self) -> None:
        os.environ["bucket_files"] = "bucket-project-cloud-storage-files"
        self.storage = CloudStorage()
    
    
    def test_upload_file_success(self):
        
        
        local_file_path = os.path.abspath("test/files/pruebas_upload_from_files.txt")
        remote_file_path  = "archivos/1/1/pruebas_upload_from_files.txt"
        
        state = self.storage.push_file( local_file_path  ,remote_file_path )
        self.assertTrue(  state)
        
    def test_download_file_success(self):
        
        local_file_path = os.path.abspath("test/files/pruebas_upload_from_files.txt")
        remote_file_path  = "archivos/1/1/pruebas_upload_from_files.txt"
        self.storage.push_file( local_file_path  ,remote_file_path )
        
        if os.path.exists(local_file_path):
            os.remove(local_file_path)
        
        
        state = self.storage.get_file( local_file_path  ,remote_file_path )
        existe_file = os.path.exists(local_file_path)
        self.assertTrue(  state  and existe_file)    
        
    
    def test_delete_file_success(self):
        remote_file_path  = "archivos/1/1/pruebas_upload_from_files.txt"
        state = self.storage.delete_file( remote_file_path )
        self.assertTrue(  state  )   
            
                