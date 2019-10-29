from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def salem():
    return "Sälem, Älem!"


@app.route('/new', methods=['POST'])
def send_swimlanes():
    json = request.get_json()
    print(json)
    socketio.emit('swimlanes', json)

    res = make_response(jsonify({'message': 'Successful!'}), 200)
    return res


if __name__ == '__main__':
    socketio.run(app)
