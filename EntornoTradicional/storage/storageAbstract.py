from abc import ABC, abstractmethod

class IStorage(ABC):
    
    @abstractmethod
    def push_file (self, fileNameLocal,fileNameRemote   ):
        pass
    
    @abstractmethod
    def get_file(self , fileNameLocal ,fileNameRemote  ):
        pass