
import zipfile
from celery import Celery
from adaptadorFormatoCompresion import AdaptadorFormatoCompresion
from zipFormatoAdapter import ZipFormatoAdapter 
from 7zFormatoAdapter import F7zFormatoAdapter
from gZipFormatoAdapter import GZipFormatoAdapter
from targzFormatoAdapter import TargzFormatoAdapter
from tarbz2FormatoAdapter import Tarbz2FormatoAdapter
from managerCompresion import ManagerCompresion
import os 
 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from models import \
    db, \
    User, convertRequest, \
    UserSchema, ConvertRequestSchema

cnstringDatabase  =  "postgres://postgres:convertir@54.226.135.40:5432/appnube" # os.environ["DATABASE_URL"]
cnstringRedis =    "redis://54.226.135.40:6379/0" # os.environ["REDIS_URL"]
app = Celery( 'tasks' , broker = cnstringRedis )

Engine = create_engine(cnstringDatabase)
Session = sessionmaker(bind=Engine)
session = Session()




@app.task
def comprimir(id_request):

        formatos = {
                'zip': ZipFormatoAdapter,
                '7z': F7zFormatoAdapter,
                'gzip': GZipFormatoAdapter
                'targz' :TargzFormatoAdapter
                'tarbz2' :Tarbz2FormatoAdapter
        }
        request = session.query(convertRequest).filter(  convertRequest.id_request == id_request ).first()
        if request.status == "uploaded" :
                formato = formatos[request.format_request]() 
                if formato not is none:
                        managerFormatoCompresion = ManagerCompresion(formato)
                        request.file_request_path =  managerFormatoCompresion.comprimir(request.file_origin_path)  
                        request.status = 'processed';                
                        session.commit()
