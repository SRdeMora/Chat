#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


from flask import Flask, request, jsonify
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
import os
app = Flask(__name__)

# Configuración de la API de Gmail
def enviar_correo(destinatario, asunto, mensaje):
from flask import Flask, request, jsonify
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
import os
import json

app = Flask(__name__)

# Configuración de la API de Gmail
def enviar_correo(destinatario, asunto, mensaje):
    # Obtener las credenciales desde la variable de entorno
    credenciales_json = os.getenv("CREDENTIALES_BOT")
    if not credenciales_json:
        raise ValueError("Las credenciales no están configuradas en las variables de entorno")
    
    creds_info = json.loads(credenciales_json)
    creds = Credentials.from_authorized_user_info(creds_info)

    # Construir el servicio de Gmail
    service = build('gmail', 'v1', credentials=creds)

    # Crear el mensaje
    message = MIMEText(mensaje)
    message['to'] = destinatario
    message['subject'] = asunto
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message = {'raw': raw}

    # Enviar el correo
    service.users().messages().send(userId="me", body=message).execute()

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    # Extraer parámetros enviados desde Dialogflow
    nombre = req['queryResult']['parameters'].get('user')
    Motivo = req['queryResult']['parameters'].get('mutivo')
    Fecha = req['queryResult']['parameters'].get('data-time')
    correo = "rasparecords@gmail.com"

    # Crear el contenido del correo
    asunto = "Confirmación de cita"
    mensaje = f"""En breve se pondrá en contacto contigo uno de nuestros profesionales para confirmar tu cita.

Hola {nombre},

Tu cita está confirmada para el {Fecha} por el motivo: {Motivo}.

Saludos."""

    # Enviar el correo
    enviar_correo(correo, asunto, mensaje)

    # Responder a Dialogflow
    fulfillment_text = f"Se ha enviado un correo de confirmación a {correo}."
    return jsonify({'fulfillmentText': fulfillment_text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

   

# In[ ]:





# In[ ]:




