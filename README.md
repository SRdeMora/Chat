<div align="center">
  <h1 align="center">
    💬 Chat Application
  </h1>
  <p align="center">
    <strong>Un proyecto de chat en tiempo real construido con Dialogflow</strong>
  </p>
</div>

<p align="center">
  <!-- Reemplaza estos badges con los que correspondan a tu proyecto -->
  <img src="https://img.shields.io/github/license/SRdeMora/Chat?style=for-the-badge" alt="Licencia">
</p>

---

## 📜 Descripción

Este es un proyecto de una aplicación de chat completamente funcional que permite a los usuarios comunicarse en tiempo real. La aplicación está diseñada para ser Samuel Rodríguez. Sirve como una demostración práctica de la implementación de websockets para comunicación bidireccional entre cliente y servidor.

<br>

<div align="center">
  <!-- IMPORTANTE: Crea un GIF o una captura de pantalla de tu app y reemplaza la URL -->
  <img src="URL_DE_TU_GIF_O_SCREENSHOT.gif" alt="Demo de la aplicación de Chat" width="700"/>
</div>

---

## ✨ Características Clave

-   **Mensajería en Tiempo Real:** Envío y recepción de mensajes instantáneos sin necesidad de recargar la página.
-   **Múltiples Salas (o Canales):** Los usuarios pueden unirse a diferentes salas de chat para conversar sobre temas específicos.
-   **Notificaciones de Conexión:** Avisos cuando un usuario se une o abandona el chat.
-   **[Añade otra característica]:** Por ejemplo, "Autenticación de usuarios".
-   **[Añade otra característica]:** Por ejemplo, "Historial de mensajes".

---

## 🛠️ Tecnologías Utilizadas

Este proyecto fue construido utilizando un stack moderno y eficiente:

-   **Backend:** Python ([Flask](https://flask.palletsprojects.com/) / [Django](https://www.djangoproject.com/)), [Node.js](https://nodejs.org/) (Elige y adapta)
-   **Comunicación en Tiempo Real:** [Socket.IO](https://socket.io/) / [WebSockets](https://developer.mozilla.org/es/docs/Web/API/WebSockets_API)
-   **Frontend:** HTML5, CSS3, Vanilla JavaScript (o [React](https://reactjs.org/), [Vue](https://vuejs.org/), etc.)
-   **Base de Datos:** [SQLite](https://www.sqlite.org/index.html) / [PostgreSQL](https://www.postgresql.org/) (Si aplica)
-   **Despliegue:** [Heroku](https://www.heroku.com/) / [Vercel](https://vercel.com/) / [Docker](https://www.docker.com/) (Si aplica)

---

## 🚀 Cómo Empezar

Sigue estos pasos para tener una copia del proyecto corriendo en tu máquina local.

### **1. Prerrequisitos**

Asegúrate de tener instalado lo siguiente:
-   Python 3.8+ (o la versión que uses)
-   Node.js y npm (si usas un framework de JS)
-   Git

### **2. Instalación**

1.  **Clona el repositorio:**
    ```sh
    git clone https://github.com/SRdeMora/Chat.git
    ```

2.  **Navega al directorio del proyecto:**
    ```sh
    cd Chat
    ```

3.  **Crea y activa un entorno virtual (recomendado para Python):**
    ```sh
    # En Windows
    python -m venv venv
    .\venv\Scripts\activate

    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Instala las dependencias del backend:**
    ```sh
    pip install -r requirements.txt
    ```
    *(Asegúrate de tener un archivo `requirements.txt` en tu repo. Si no lo tienes, créalo con `pip freeze > requirements.txt`)*

5.  **Instala las dependencias del frontend (si aplica):**
    ```sh
    # Si usas Node.js para el frontend (ej. con React)
    # cd frontend
    # npm install
    ```

### **3. Configuración del Entorno**

Crea un archivo `.env` en la raíz del proyecto y añade las variables de entorno necesarias.

https://srdemora.github.io/Chat/
