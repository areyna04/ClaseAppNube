from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import json 
import hashlib
import base64
import os

from models import \
    db, \
    User, convertRequest, \
    UserSchema, ConvertRequestSchema

user_schema = UserSchema()
convert_request_schema = ConvertRequestSchema()

class AdminUsers():
    def create_user(self ,   usuario : str  , pwd : str, email : str ): 
        contrasena_encriptada = hashlib.md5(pwd.encode('utf-8')).hexdigest()
        nuevo_usuario = User(user=usuario , passwd=contrasena_encriptada, email=email)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {"mensaje": "usuario creado exitosamente", "id": nuevo_usuario.id}

admin_user = AdminUsers()


class VistaSignIn(Resource):

    def post(self):
        usuario = User.query.filter(User.user == request.json["usuario"]).first()
        if usuario is None:
            
            nuevo_usuario = admin_user.create_user(request.json["usuario"]  , request.json["contrasena"] , request.json["email"]   )
            return {"mensaje": "usuario creado exitosamente", "id": nuevo_usuario["id"]}
        else:
            return "El usuario ya existe", 404

    def put(self, id_usuario):
        usuario = User.query.get_or_404(id_usuario)
        usuario.contrasena = request.json.get("contrasena", usuario.contrasena)
        db.session.commit()
        return user_schema.dump(usuario)

    def delete(self, id_usuario):
        usuario = User.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204

class VistaLogIn(Resource):
    def post(self):

        contrasena_encriptada = hashlib.md5(request.json["contrasena"].encode('utf-8')).hexdigest()
        user = User.query.filter(User.user == request.json["usuario"],
                                    User.passwd == contrasena_encriptada).first()
        if user is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=user.id)
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso, "id": user.id}
    
    def delete(self):
        db.session.close()
        db.session.close_all()
        return '', 204
    
class VistaTasks(Resource):
    @jwt_required()
    def get(self):
        user = request.json["id_user"]
        max = request.json["max"]
        if(max.isnumeric):
            if(request.json["order"]=="1"):
                convertRequests = convertRequest.query.filter(convertRequest.id_user==user).order_by(convertRequest.id_request.desc()).limit(int(max)).all()
            else:
                convertRequests = convertRequest.query.filter(convertRequest.id_user==user).order_by(convertRequest.id_request.asc()).limit(int(max)).all()
            return [convert_request_schema.dump(convertRequest) for convertRequest in convertRequests]
        else:
            return {"cod": "ER002", "error": "el número maximo de registros debe ser un número" }
        

    @jwt_required()
    def post(self):
        file_name=request.json["file_name"]
        resp=""
        user = request.json["id_user"]
        user_path="files/"+user 
        if not os.path.isdir(user_path ):
            os.makedirs(user_path)

        new_convertRequest = convertRequest( \
            id_user = request.json["id_user"], \
            format_request = request.json["format_request"]
        )

        db.session.add(new_convertRequest)
        db.session.flush()
        file_origin_path=user_path+"/"+ str(new_convertRequest.id_request) 
        os.makedirs(file_origin_path)
        file_origin_path=file_origin_path+"/"+file_name
        new_convertRequest.file_origin_path= file_origin_path
        file_b64=request.json["file_b64"]
        with open(file_origin_path, "wb") as fh:
            fh.write(base64.b64decode(file_b64))
        if(os.path.exists(file_origin_path)):
            db.session.commit()  
            resp=convert_request_schema.dump(new_convertRequest)
        else:
            db.session.rollback()
            resp= {"cod": "ER001", "error": "Error al procesar archivo", "id_trasaction": new_convertRequest.id_request }
        
        
        return resp
        
class VistaFile(Resource):
    @jwt_required()
    def get(self, id_request):
        convertRequests = convertRequest.query.get_or_404(id_request)
        if(request.json["original_file"]=="1"):
           path=  convertRequests.file_origin_path  
        elif(request.json["original_file"]=="0"):
            path=  convertRequests.file_origin_path
        else:
            return {"cod": "ER003", "error": "Error en parametro"}
        with open(path, 'rb') as file:
            content = file.read()
            b64file = base64.b64encode(content)
        datos = {
            "file": b64file.decode()
        }
        return datos
