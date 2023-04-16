
import zipfile
from celery import Celery

app = Celery( 'tasks' , broker = 'redis://redis:6379/0' )


@app.task
def test_tarea(nombre):
        return '\n--->Se agrega tarea de prueba!!!: %s' % nombre

@app.task
def comprimir(filename, zipname, new_path):
    print ('\n-> Se va a comprimir el archivo: {}'.format(filename))
    zfile = zipfile.ZipFile(new_path + '/' + zipname, 'w')
    zfile.write(filename, compress_type = zipfile.ZIP_DEFLATED)
    zfile.close()
    print ('\n-> El archivo comprimido se copió a : {}'.format(new_path))

