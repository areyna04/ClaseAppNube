import tarfile
import os

from AdaptadorFormatoCompresion import AdaptadorFormatoCompresion 

class Tarbz2FormatoAdapter( AdaptadorFormatoCompresion) :

    def comprimir(self, input_file, output_file):
        with tarfile.open(output_file, "w:bz2") as tar:
            tar.add(input_file, arcname="")
    
    def descomprimir(self, input_file, output_path):
        with tarfile.open(input_file, "r:bz2") as tar:
            tar.extractall(output_path)
                
    def dar_extension(self) -> string :
        return  "tar.bz2"             
