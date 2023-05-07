
import io
import zipfile
from storage.cloudStorage import CloudStorage
from  admin_files.ManagerFiles  import ManagerFiles
from celery import Celery
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
cnstringRedis =      os.environ.get("REDIS_URL") # "redis://localhost:6379/0" # os.environ["REDIS_URL"]
app = Celery( 'tasks' , broker = cnstringRedis )

Engine = create_engine(cnstringDatabase)
Session = sessionmaker(bind=Engine)
session = Session()

storage = CloudStorage()
manager_files = ManagerFiles(storage)


@app.task(bind=True, autoretry_for=(Exception), retry_kwargs={'max_retries': 7, 'countdown': 5})
def comprimir(id_request):
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

                                aux_path =  f"/{request.id_user }/{id_request}"  
                                proceso_ok,  remote_path  , mensaje=  manager_files.sync(aux_path ,local_path_request_file_name , manager_files.get_file_base64(local_path_request)  )   
                                if  not proceso_ok :
                                        raise Exception(mensaje)
                                
                                request.file_request_path = remote_path
                                request.status = 'processed';                
                                session.commit()
                                os.remove(local_path)  
                                os.removedirs(os.path.dirname(local_path))
        except Exception as ext:    
                error =f"Unexpected {ext=}, {type(ext)=}"    
                print(error)
                raise           