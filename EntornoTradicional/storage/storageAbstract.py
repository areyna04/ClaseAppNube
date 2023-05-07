from abc import ABC, abstractmethod

class IStorage(ABC):
    
    @abstractmethod
    def push_file (self, file_name_local ,file_name_remote    ):
        pass
    
    @abstractmethod
    def get_file(self , file_name_local ,file_name_remote  ):
        pass
    
    @abstractmethod 
    def delete_file(self , file_name_remote    ):
        pass
    @abstractmethod 
    def exists_file(self , file_name_remote    ):
        pass