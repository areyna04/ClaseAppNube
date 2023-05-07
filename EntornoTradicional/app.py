from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
import os
from views.views import VistaTasksGet, VistaTasksPost 
from models import db
from views import \
    VistaSignIn, VistaLogIn, VistaTasks, VistaFile, VistaTask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get("SQLALCHEMY_DATABASE_URI")   # "postgresql://postgres:convert@54.86.141.90:5432/appnube"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)

api.add_resource(VistaSignIn, '/api/auth/signup')
api.add_resource(VistaLogIn, '/api/auth/login')
api.add_resource(VistaTasksPost, '/api/tasks')
api.add_resource(VistaTasksGet, '/api/tasks/<string:user>/<string:max>/<string:order>')
api.add_resource(VistaFile, '/api/file/<int:id_request>/<string:original_file>')
api.add_resource(VistaTask, '/api/task/<int:id_request>')
jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')