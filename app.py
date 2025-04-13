from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdjklhasdf'

socketio = SocketIO(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping')
def ping():
    socketio.emit('response', [request.remote_addr, dict(request.headers)])
    return 'Ping Success\n'


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)