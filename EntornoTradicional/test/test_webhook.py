
import unittest
from  EntornoTradicional.app   import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Crea un cliente de prueba para interactuar con la aplicación
        self.client = app.test_client()
        # Activa el contexto de prueba
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Elimina el contexto de prueba
        self.app_context.pop()

    def test_webhook(self):
        # Define los datos JSON para enviar en la solicitud POST
        data = {'message':  { 'data': '5' }}
        # Envía una solicitud POST a la ruta '/saludo' con los datos JSON
        response = self.client.post('/api/task/webhook', json=data)
        # Verifica que la respuesta sea exitosa (código 200)
        self.assertEqual(response.status_code, 200)
       
