#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[7]:


from flask import Flask, request, jsonify
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText

app = Flask(__name__)

# Configuración de la API de Gmail
def enviar_correo(destinatario, asunto, mensaje):
    creds = Credentials.from_authorized_user_file('credenciales_bot.json')  # Tu archivo de credenciales
    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(mensaje)
    message['to'] = destinatario
    message['subject'] = asunto
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message = {'raw': raw}

    service.users().messages().send(userId="me", body=message).execute()

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    # Extraer parámetros enviados desde Dialogflow
    nombre = req['queryResult']['parameters'].get('nombre')
    fecha = req['queryResult']['parameters'].get('fecha')
    hora = req['queryResult']['parameters'].get('hora')
    correo="rasparecords@gmail.com"
    # Crear el contenido del correo
    asunto = "Confirmación de cita"
    mensaje = f"Hola {nombre},\n\nTu cita está confirmada para el {fecha} a las {hora}.\n\nSaludos."

    # Enviar el correo
    enviar_correo(correo, asunto, mensaje)

    # Responder a Dialogflow
    fulfillment_text = f"Se ha enviado un correo de confirmación a {correo}."
    return jsonify({'fulfillmentText': fulfillment_text})

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




