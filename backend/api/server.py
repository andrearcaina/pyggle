from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def read_root():
    return jsonify({"Hello": "World"})

if __name__ == "__main__":
    app.run(port=5000)