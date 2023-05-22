import base64
from worker.WorkerCompresion import TareaCompresion

from flask import Flask, request


app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    envelope = request.get_json()
    if not envelope:
        msg = "no Pub/Sub message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(envelope, dict) or "message" not in envelope:
        msg = "invalid Pub/Sub message format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    pubsub_message = envelope["message"]

    id_request = ""
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        tarea =  TareaCompresion()
        id_request = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
        print(f'procesando mensaje   {id_request} ' )
        resultado_ok= tarea.comprimir(id_request)
        print(f'estado proceso  {id_request} : {resultado_ok}  ' )
        if not resultado_ok :
            return f"Server Error: {msg}", 504
        
    print(f"Tarea procesada {id_request}!")

    return ("", 204)

