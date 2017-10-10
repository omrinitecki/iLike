from flask import Flask
from flask import jsonify
from flask import request
import paho.mqtt.client as mqtt


app = Flask(__name__)
client = mqtt.Client("gduitmnm")
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
    client.connect("m12.cloudmqtt.com")
    app.run(debug=True)


if __name__ == "__main__":
    main()
