from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from api.helpers.get_boggle import found_words, coordinates, scores
# from api.helpers.detect_img import * 
# commented out detect_img for testing purposes

app = FastAPI()

# CORS middleware to Next.js host number
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"],
    allow_credentials=True, 
    allow_methods=["*"], # allow all HTTP methods 
    allow_headers=["*"]
)

# testing purposes
@app.get("/api/data")
async def return_data():
    result = {"Hello": "World!"}
    return JSONResponse(content=result, status_code=200)

@app.get("/api/words/{board}")
async def return_words(board: str, words: Union[str, None] = None, official: bool = False):
    all_words = found_words(board, words, official)
    return JSONResponse(content=all_words, status_code=200)

@app.get("/api/coords/{board}")
async def return_coords(board: str, words: Union[str, None] = None, official: bool = False):
    all_coords = coordinates(board, words, official)
    return JSONResponse(content=all_coords, status_code=200)

@app.get("/api/scores/{board}")
async def return_coords(board: str, words: Union[str, None] = None, official: bool = False):
    all_scores = scores(board, words, official)
    return JSONResponse(content=all_scores, status_code=200)

@app.post("/api/detect") # post method cuz of update of image/data
async def return_image():
    return {"image": "detection"}
