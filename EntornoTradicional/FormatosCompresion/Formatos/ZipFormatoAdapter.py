import zipfile
import io
from AdaptadorFormatoCompresion import AdaptadorFormatoCompresion 

class ZipFormatoAdapter( AdaptadorFormatoCompresion) :

    def comprimir(self, input_file, output_file):
        with zipfile.ZipFile(output_file , mode= "w" , compression= zipfile.ZIP_DEFLATED ) as zipf :
            zipf.write(input_file )

    
    def descomprimir(self, input_file, output_path):
        with zipfile.ZipFile( input_file ,  mode= "r"  ) as zipf :
            zipf.extractall(output_path)
    
    
    def dar_extension(self) -> string :
        return  "zip"      