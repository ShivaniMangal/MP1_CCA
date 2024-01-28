import socket
import subprocess

from flask import Flask, request, jsonify

app = Flask(__name__)
seed_value = 0


@app.route('/', methods=['GET', 'POST'])
def web_server_app():
    global seed_value

    if request.method == 'GET':
        return socket.gethostname()

    elif request.method == 'POST':
        subprocess.Popen(["python", "stress_cpu.py"])
        return "Stress Test Started"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
