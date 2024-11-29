from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Flask App!"


@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello, Jenkins + Flask!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)