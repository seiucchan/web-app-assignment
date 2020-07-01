from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def heelo_world():
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True, port=8000, threaded=True) 
