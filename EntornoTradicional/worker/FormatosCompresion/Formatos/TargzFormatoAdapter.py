import tarfile
import os

from worker.FormatosCompresion.Formatos.AdaptadorFormatoCompresion  import AdaptadorFormatoCompresion 

class TargzFormatoAdapter( AdaptadorFormatoCompresion) :

    def comprimir(self, input_file, output_file):
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(input_file, arcname="")
    
    def descomprimir(self, input_file, output_path):
        with tarfile.open(input_file, "r:gz") as tar:
            tar.extractall(output_path)
                
        
    def dar_extension(self):
        return  "tar.gz"      