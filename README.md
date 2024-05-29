<h1 align="center">
  <img src="client/public/pyggle_logo - white.png" alt="logo" width="50%">
</h1>

# Pyggle

Find all possible words given a boggle board and words (or none!), with a visual representation on how the algorithm works on the web!

Web Demo: [Coming Soon!](https://github.com/andrearcaina/pyggle)

## Tech Stack

[![TYPESCRIPT](https://img.shields.io/badge/typescript-3178C6?style=for-the-badge&logo=typescript&logoColor=FFF)](https://www.typescriptlang.org/)
[![NEXT.JS](https://img.shields.io/badge/NEXT-0769AD?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![TAILWINDCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/) \
The frontend is developed using `TypeScript` and the Next.js framework, with Tailwind CSS as the chosen `CSS` framework.

[![PYTHON](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FASTAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![EasyOCR](https://img.shields.io/badge/easyocr-008080?style=for-the-badge&logo=python&logoColor=white) \
The backend framework chosen for this project is FastAPI, a performant `Python`-based web framework. In FastAPI, I create API endpoints to communicate with the frontend (the client).
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

Input is case sensitive (for the board). 

The input would consist of: an N x M board as a string with rows separated by spaces. Alternatively, you can pass in a list of lists where each element is the character on the board.

If words is not passed as an argument, it will utilize a text file that consists of [479k](https://github.com/dwyl/english-words) words. 

If official is not given as a boolean argument, find all words regardless of length, and the letter 'Q' is not represented as 'Qu'.
If official is passed as a boolean argument, then the algorithm follows the official rules of boggle. Pyggle will solve and:
- find all words that have a length greater than 3.
- The letter 'Q' is now represented as 'Qu'.

```python
from pyggle import Boggle

board = "ea st"

boggle = Boggle(board)

boggle.print_result()
```

For more functions from `pyggle`, check:
- [`lib/examples/2x2_example.py`](https://github.com/andrearcaina/pyggle/blob/main/lib/examples/2x2_example.py) for general functions and more specificity
- [`lib/examples/qu_example.py`](https://github.com/andrearcaina/pyggle/blob/main/lib/examples/qu_example.py) for an example where the letter 'Q' represents 'Qu'
- [`lib/docs/boggle-api.md`](https://github.com/andrearcaina/pyggle/blob/main/lib/docs/boggle-api.md) for an understanding of each method

### Output

I don't know how "ae" or "aes" or "ast" is a word, but w/e :P

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
