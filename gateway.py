from flask import Flask
from flask import jsonify
from flask import request
import paho.mqtt.client as mqtt
import os


app = Flask(__name__)
broker_address = os.environ.get("mqtt-host", "")
port = int(os.environ.get("mqtt-port", ""))
user = os.environ.get("mqtt-user", "")
password = os.environ.get("mqtt-pwd", "")
client = mqtt.Client("Python")
messages = []


@app.route('/', methods=['GET'])
def return_all():
    return jsonify({'messages': messages})


@app.route('/', methods=['POST'])
def addOne():
    message = request.get_json()
    client.publish("python/test", str(message))
    messages.append(message)
    return jsonify({'messages': messages})


def main():
    client.username_pw_set(user, password=password)
    client.connect(broker_address, port=port)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


if __name__ == "__main__":
    main()
