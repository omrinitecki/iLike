from flask import Flask
from flask import jsonify
from flask import request
import paho.mqtt.client as mqtt
import os
from datetime import datetime


app = Flask(__name__)
broker_address = str(os.environ["MQTT-HOST"])
port = int(os.environ["MQTT-PORT"])
user = str(os.environ.get["MQTT-USER"])
password = str(os.environ["MQTT-PWD"])
client = mqtt.Client("Python")
messages = []


@app.route('/', methods=['GET'])
def return_all():
    return jsonify({'messages': messages})


@app.route('/', methods=['POST'])
def addOne():
    message = jsonify({request.get_data(): datetime.now()})
    client.publish("python/test", str(message))
    messages.append(message)
    return jsonify({'messages': messages})


def main():
    client.username_pw_set(user, password=password)
    client.connect(broker_address, port=port)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


if __name__ == "__main__":
    main()
