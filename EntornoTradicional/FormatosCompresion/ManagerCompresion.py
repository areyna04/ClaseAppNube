from adaptadorFormatoCompresion import AdaptadorFormatoCompresion
import io

class  ManagerCompresion( ): 
    def __init__(self, adapter):
        self.adapter = adapter
    
    def comprimir(self, input_file) -> string :
        path_sin_extencion = os.path.splitext(input_file )[0]
        output_file =  f"{path_sin_extencion}.{self.adapter.dar_extension()}"
        self.adapter.compress(input_file, output_file)
        return output_file

    def descomprimir(self, input_file, output_path):
        self.adapter.decompress(input_file, output_path)