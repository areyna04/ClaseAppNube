
import zipfile
from celery import Celery
from AdaptadorFormatoCompresion
from ZipFormatoAdapter
from F7zFormatoAdapter
from GZipFormatoAdapter
from TargzFormatoAdapter
from Tarbz2FormatoAdapter
from ManagerCompresion

from models import \
    db, \
    User, convertRequest, \
    UserSchema, ConvertRequestSchema

app = Celery( 'tasks' , broker = 'redis://redis:6379/0' )

@app.task
def comprimir(id_request):

        formatos = {
                'zip': ZipFormatoAdapter,
                '7z': F7zFormatoAdapter,
                'gzip': GZipFormatoAdapter
                'targz' :TargzFormatoAdapter
                'tarbz2' :Tarbz2FormatoAdapter
        }
        request = convertRequest.query.filter(  convertRequest.id_request == id_request ).first()
        if request.status == "uploaded" :
        formato = formatos[request.format_request]() 
        if formato not is none:
                managerFormatoCompresion = ManagerCompresion(formato)
                request.file_request_path =  managerFormatoCompresion.comprimir(request.file_origin_path)  
                request.status = 'processed';                
                db.session.add()
                db.session.flush()
