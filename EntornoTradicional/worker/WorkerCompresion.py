import io
import zipfile
from storage.cloudStorage import CloudStorage
from  admin_files.ManagerFiles  import ManagerFiles

from  worker.FormatosCompresion.Formatos.AdaptadorFormatoCompresion  import AdaptadorFormatoCompresion
from  worker.FormatosCompresion.Formatos.ZipFormatoAdapter  import ZipFormatoAdapter 
from  worker.FormatosCompresion.Formatos.F7zFormatoAdapter import F7zFormatoAdapter
from  worker.FormatosCompresion.Formatos.GZipFormatoAdapter import GZipFormatoAdapter
from  worker.FormatosCompresion.Formatos.TargzFormatoAdapter import TargzFormatoAdapter
from  worker.FormatosCompresion.Formatos.Tarbz2FormatoAdapter import Tarbz2FormatoAdapter
from  worker.FormatosCompresion.ManagerCompresion import ManagerCompresion 
import os 
import base64

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session , sessionmaker
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema , auto_field
from sqlalchemy import Column, Identity
from sqlalchemy import Table
from sqlalchemy import ForeignKey
import datetime


from models import \
    db, \
    User, convertRequest, \
    UserSchema, ConvertRequestSchema


cnstringDatabase  =  os.environ.get("SQLALCHEMY_DATABASE_URI")   #    "postgresql://postgres:convert@54.86.141.90:5432/appnube" # os.environ["DATABASE_URL"]
Engine = create_engine(cnstringDatabase)
Session = sessionmaker(bind=Engine)
session = Session()

storage = CloudStorage()
manager_files = ManagerFiles(storage)


class TareaCompresion() :

        def comprimir(self, id_request):
                try:
                        print (f" recibiendo id {id_request}  ")
                        formatos = {
                                'zip': ZipFormatoAdapter,
                                '7z': F7zFormatoAdapter,
                                'gzip': GZipFormatoAdapter,
                                'targz' :TargzFormatoAdapter,
                                'tarbz2' :Tarbz2FormatoAdapter
                        }
                        request = session.query(convertRequest).filter(  convertRequest.id_request == id_request ).first()
                        if request.status == "uploaded" :
                                formato = formatos[request.format_request]() 
                                if (formato is not None):
                                        managerFormatoCompresion = ManagerCompresion(formato)
                                        
                                        proceso_ok,  local_path ,   mensaje=  manager_files.get_file(request.file_origin_path)       
                                        if  not proceso_ok :
                                                raise Exception(mensaje)
                                        local_path_request  =  managerFormatoCompresion.comprimir(local_path) 
                                        local_path_request_file_name  = os.path.basename(local_path_request)

                                        aux_path =  f"files/{request.id_user }/{id_request}"  
                                        proceso_ok,  remote_path  , mensaje=  manager_files.sync(aux_path ,local_path_request_file_name , manager_files.get_file_base64(local_path_request)  )   
                                        if  not proceso_ok :
                                                raise Exception(mensaje)
                                        
                                        request.file_request_path = remote_path
                                        request.status = 'processed';                
                                        session.commit()
                                        manager_files.delete_local_file(local_path) 
                                        manager_files.delete_local_file(local_path_request) 
                                        return True 
                except Exception as ext:    
                        error =f"Unexpected {ext=}, {type(ext)=}"    
                        print(error)
                        return False       

                                