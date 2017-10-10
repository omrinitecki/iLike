from flask import Flask
from flask import jsonify
from flask import request
import paho.mqtt.client as mqtt
import os


app = Flask(__name__)
broker_address = "m12.cloudmqtt.com"
port = "17516"
user = "gduitmnm"
password = "XbW2LU2qZZIo"
client = mqtt.Client("Omri")
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
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)


if __name__ == "__main__":
    main()
