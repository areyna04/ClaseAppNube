+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from models import db
from views import \
    VistaSignIn, VistaLogIn, VistaTasks, VistaFile, VistaTask

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:wilson@localhost:5432/appnube"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:convert@54.86.141.90:5432/appnube"
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
api.add_resource(VistaTasks, '/api/tasks')
api.add_resource(VistaFile, '/api/file/<int:id_request>')
api.add_resource(VistaTask, '/api/task/<int:id_request>')
jwt = JWTManager(app)