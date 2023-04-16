import tarfile
import os

from AdaptadorFormatoCompresion import AdaptadorFormatoCompresion 

class Tarbz2FormatoAdapter( AdaptadorFormatoCompresion) :

    def comprimir(self, input_file, output_file):
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(input_file, arcname="")
    
    def descomprimir(self, input_file, output_path):
        with tarfile.open(input_file, "r:gz") as tar:
            tar.extractall(output_path)
                
