from doctest import debug

from flask import Flask, render_template, make_response, request, send_from_directory
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
from datetime import datetime
import os
import subprocess
import sys

app = Flask(__name__)

# cors = CORS()
# cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

# socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def indexRoute():
    return "cectado"

@socketio.on('connect')
def test_connect():
    print("client Connected")
    # emit('message', "emit test")

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print(data)
    socketio.emit('message', data)

if __name__ == '__main__':
    # app.run(debug=True, port=5454, host="0.0.0.0")
    socketio.run(app, debug=True, port=7667, host="0.0.0.0")
