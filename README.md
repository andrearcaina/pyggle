<h1 align="center">
  <img src="backend/data/images/test2.png" alt="logo" width="50%">
</h1>

# Pyggle
Find all possible words given a boggle board and words (or none!), with a visual representation on how the algorithm works!

Web Demo: [Coming Soon!](https://github.com/andrearcaina/pyggle)

## Tech Stack
[![JAVASCRIPT](https://img.shields.io/badge/typescript-3178C6?style=for-the-badge&logo=typescript&logoColor=FFF)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![NEXT.JS](https://img.shields.io/badge/NEXT-0769AD?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![TAILWINDCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/) \
The frontend is developed using `TypeScript` and the Next.js framework, with Tailwind CSS as the chosen `CSS` framework.

[![PYTHON](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FLASK](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/3.0.x/)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![EasyOCR](https://img.shields.io/badge/easyocr-008080?style=for-the-badge&logo=python&logoColor=white) \
The backend framework chosen for this project is Flask, a `Python`-based framework. In Flask, I create API endpoints to communicate with the frontend (the client).
These endpoints are designed to decipher the given boggle board from the client and return all possible combinations, coordinates, and score using **Pyggle**. 
The user can also send an image of a boggle board where I use **OpenCV** to preprocess the image and use **EasyOCR** to accurately retrieve the characters from the boggle board.

The words and coordinates are then sent to the client as a JSON payload for the frontend to render.

## Package

PyPi: [https://pypi.org/project/pyggle/](https://pypi.org/project/pyggle/)

## Installation

```bash
pip install pyggle
```

## Usage
```python
from pyggle import Boggle

board = [['e', 'a'], ['s', 't']]

# if words is not passed as an argument of type list, will utilize 479k words (all in English)
# if official is not given as a boolean argument, find all words regardless of length
boggle = Boggle(board)

# prints word: [coords of each character] format.
boggle.print_result()
```
For more functions from `pyggle`, check [`lib/examples/example.py`](https://github.com/andrearcaina/pyggle/blob/main/lib/examples/example.py) or [`lib/docs/api-reference.md`](https://github.com/andrearcaina/pyggle/blob/main/lib/docs/api-reference.md)

### Output
I don't know how "ae" or "aes" or "ast" is a word, but here is where I got the [479k word list](https://github.com/dwyl/english-words)
```bash
a: [(0, 1)]
ae: [(0, 1), (0, 0)]
aes: [(0, 1), (0, 0), (1, 0)]
aet: [(0, 1), (0, 0), (1, 1)]
as: [(0, 1), (1, 0)]
ase: [(0, 1), (1, 0), (0, 0)]
ast: [(0, 1), (1, 0), (1, 1)]
at: [(0, 1), (1, 1)]
ate: [(0, 1), (1, 1), (0, 0)]
ates: [(0, 1), (1, 1), (0, 0), (1, 0)]
e: [(0, 0)]
ea: [(0, 0), (0, 1)]
east: [(0, 0), (0, 1), (1, 0), (1, 1)]
eat: [(0, 0), (0, 1), (1, 1)]
eats: [(0, 0), (0, 1), (1, 1), (1, 0)]
es: [(0, 0), (1, 0)]
est: [(0, 0), (1, 0), (1, 1)]
et: [(0, 0), (1, 1)]
eta: [(0, 0), (1, 1), (0, 1)]
etas: [(0, 0), (1, 1), (0, 1), (1, 0)]
s: [(1, 0)]
sa: [(1, 0), (0, 1)]
sae: [(1, 0), (0, 1), (0, 0)]
sat: [(1, 0), (0, 1), (1, 1)]
sate: [(1, 0), (0, 1), (1, 1), (0, 0)]
se: [(1, 0), (0, 0)]
sea: [(1, 0), (0, 0), (0, 1)]
seat: [(1, 0), (0, 0), (0, 1), (1, 1)]
set: [(1, 0), (0, 0), (1, 1)]
seta: [(1, 0), (0, 0), (1, 1), (0, 1)]
st: [(1, 0), (1, 1)]
sta: [(1, 0), (1, 1), (0, 1)]
t: [(1, 1)]
ta: [(1, 1), (0, 1)]
tae: [(1, 1), (0, 1), (0, 0)]
tas: [(1, 1), (0, 1), (1, 0)]
te: [(1, 1), (0, 0)]
tea: [(1, 1), (0, 0), (0, 1)]
teas: [(1, 1), (0, 0), (0, 1), (1, 0)]
ts: [(1, 1), (1, 0)]
```

