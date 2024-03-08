from fastapi import FastAPI
from typing import Union
from api.helpers.get_boggle import possibilities as boggle_possibilities
# from api.helpers.detect_img import * 
# commented out detect_img for testing purposes

app = FastAPI()

@app.get("/api/words")
async def return_words(board: str, words: Union[str, None] = None):
    return boggle_possibilities(board, True, words)

@app.get("/api/coords")
async def return_coords(board: str, words: Union[str, None] = None):
    return boggle_possibilities(board, False, words)

@app.get("/api/detect")
async def return_image():
    return {"image": "detection"}
