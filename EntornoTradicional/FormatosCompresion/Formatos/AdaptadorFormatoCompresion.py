from abc import ABC, abstractmethod

class AdaptadorFormatoCompresion(ABC):
    @abstractmethod
    def comprimir(self, input_file, output_file):
        pass

    @abstractmethod
    def descomprimir(self, input_file, output_path):
        pass
    