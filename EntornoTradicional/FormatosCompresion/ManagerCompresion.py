from AdaptadorFormatoCompresion import AdaptadorFormatoCompresion


class  ManagerCompresion( AdaptadorFormatoCompresion): 
    def __init__(self, adapter):
        self.adapter = adapter
    
    def comprimir(self, input_file, output_file):
        self.adapter.compress(input_file, output_file)

    def descomprimir(self, input_file, output_path):
        self.adapter.decompress(input_file, output_path)