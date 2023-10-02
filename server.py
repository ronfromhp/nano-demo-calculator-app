from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    request_data = request.get_json()
    first = int(request_data['first'])
    second = int(request_data['second'])
    return jsonify({'result': first + second})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    request_data = request.get_json()
    first = int(request_data['first'])
    second = int(request_data['second'])
    return jsonify({'result': first - second})


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
