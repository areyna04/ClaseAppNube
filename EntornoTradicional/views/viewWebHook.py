
from flask import request
from worker.WorkerCompresion import TareaCompresion
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
import base64
import json



class VistaWebHook(Resource):

    def post(self):
       mensaje = json.loads(request.json)
       ok  = self.comprimir_callback(mensaje)
       if ok :
           return 200
       else: 
           return f"Error comprimiendo archivo {mensaje.data} ", 500


    def comprimir_callback (self, mensaje):    
        tarea =  TareaCompresion()
        id_request = mensaje.data.decode('utf-8')
        print(f'procesando mensaje   {id_request} ' )

        resultado_ok= tarea.comprimir(id_request)
        print(f'estado proceso  {id_request} : {resultado_ok}  ' )
        return resultado_ok
                        
               
    
