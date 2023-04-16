import gzip
import io
from AdaptadorFormatoCompresion import AdaptadorFormatoCompresion 

class GZipFormatoAdapter( AdaptadorFormatoCompresion) :

    def comprimir(self, input_file, output_file):
        with gzip.open(input_file , mode= "rb") as f_in  :
            with gzip.open(output_file, mode= "wb" ) as f_out: 
                f_out.write(f_in.read())

    
    def descomprimir(self, input_file, output_path):
        with gzip.open(input_file, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                f_out.write(f_in.read())
                
     def dar_extension(self) -> string :
        return  "gzip"                

    