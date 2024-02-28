from flask import Flask, jsonify, request
from helpers.get_boggle import possibilities
from helpers.detect_img import *

app = Flask(__name__)

@app.route("/api/words")
def return_words():
    board = request.args.get('board')
    words = request.args.get('words') or None

    return jsonify(possibilities(board, True, words))

@app.route("/api/coords")
def return_coords():
    board = request.args.get('board')
    words = request.args.get('words') or None

    return jsonify(possibilities(board, False, words))

@app.route("/api/detect")
def return_image():
    return jsonify({"image": "detection"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)