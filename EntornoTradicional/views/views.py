from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import json 
import hashlib

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
