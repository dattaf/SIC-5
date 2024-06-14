import json
from flask import Flask, request, jsonify

app = Flask(__name__)

UDARA_DATA = []

@app.route("/")
def root_route():
    return "Hello world!"

@app.route("/udara")
def get_udara():
    return jsonify(UDARA_DATA)

@app.route("/submit-udara", methods=["POST"])
def post_udara():
    pesan = request.data.decode("utf8")
    UDARA_DATA.append(float(pesan))
    print(pesan)
    return f"Received udara {pesan}"

@app.route("/submit", methods=["POST"])
def post_data():
    pesan = request.data.decode("utf8")
    pesan = json.loads(pesan)
    UDARA_DATA.append(float(pesan["udara"]))
    print(pesan)
    return f"Received data {pesan}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
