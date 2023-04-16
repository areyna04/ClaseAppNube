
import zipfile
from celery import Celery
from AdaptadorFormatoCompresion
from ZipFormatoAdapter
from F7zFormatoAdapter
from GZipFormatoAdapter
from TargzFormatoAdapter
from Tarbz2FormatoAdapter
from ManagerCompresion
import os 
 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from models import \
    db, \
    User, convertRequest, \
    UserSchema, ConvertRequestSchema

cnstringDatabase  = os.environ["DATABASE_URL"]
cnstringRedis = os.environ["REDIS_URL"]
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
