from abc import ABC, abstractmethod

class IStorage(ABC):
    
    @abstractmethod
    def push_file (self, file ):
        pass
    
    @abstractmethod
    def get_file(self , file ):
        pass