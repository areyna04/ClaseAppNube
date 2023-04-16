import pylzma
import os

from AdaptadorFormatoCompresion import AdaptadorFormatoCompresion 

class F7zFormatoAdapter( AdaptadorFormatoCompresion) :

    def comprimir(self, input_file, output_file):
        with pylzma.open(output_file, mode='wb') as output_file:
            # Escribir los datos comprimidos en el archivo
            output_file.write(input_file.read())
    
    def descomprimir(self, input_file, output_path):
        # Abrir el archivo comprimido 7Z
        with pylzma.open(input_file, mode='rb') as input_file:
            # Crear el archivo descomprimido
            with open(output_path, 'wb') as output_file:
                # Escribir los datos descomprimidos en el archivo
                output_file.write(input_file.read())

    def dar_extension(self) -> string :
        return  "7z"            
                
