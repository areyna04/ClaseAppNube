
from flask import request
from worker.WorkerCompresion import TareaCompresion
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
import base64
import json



class VistaWebHook(Resource):

    def post(self):
       mensaje =  request.get_json()
       ok  = self.comprimir_callback(mensaje["message"]["data"])
       if ok :
           return 200
       else: 
           return f"Error comprimiendo archivo {mensaje} ", 500


    def comprimir_callback (self, mensaje):    
        tarea =  TareaCompresion()
        binary_request  = base64.b64decode(mensaje)   ##mensaje.data.decode('utf-8')
        id_request = binary_request.decode().strip()

        print(f'procesando mensaje   {id_request} ' )

        resultado_ok= tarea.comprimir(id_request)
        print(f'estado proceso  {id_request} : {resultado_ok}  ' )
        return resultado_ok
                        
               
    
