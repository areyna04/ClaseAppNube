
import zipfile
from celery import Celery
from  worker.FormatosCompresion.Formatos.AdaptadorFormatoCompresion  import AdaptadorFormatoCompresion
from  worker.FormatosCompresion.Formatos.ZipFormatoAdapter  import ZipFormatoAdapter 
from  worker.FormatosCompresion.Formatos.F7zFormatoAdapter import F7zFormatoAdapter
from  worker.FormatosCompresion.Formatos.GZipFormatoAdapter import GZipFormatoAdapter
from  worker.FormatosCompresion.Formatos.TargzFormatoAdapter import TargzFormatoAdapter
from  worker.FormatosCompresion.Formatos.Tarbz2FormatoAdapter import Tarbz2FormatoAdapter
from  worker.FormatosCompresion import ManagerCompresion 
import os 
 



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

cnstringDatabase  =  "postgresql://postgres:convert@54.226.135.40:5432/appnube" # os.environ["DATABASE_URL"]
cnstringRedis =    "redis://localhost:6379/0" # os.environ["REDIS_URL"]
app = Celery( 'tasks' , broker = cnstringRedis )

Engine = create_engine(cnstringDatabase)
Session = sessionmaker(bind=Engine)
session = Session()

@app.task
def comprimir(id_request):

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
                if formato is not  none:
                        managerFormatoCompresion = ManagerCompresion(formato)
                        request.file_request_path =  managerFormatoCompresion.comprimir(request.file_origin_path)  
                        request.status = 'processed';                
                        session.commit()
