<h1 align="center">
  <img src="backend/data/images/test2.png" alt="logo" width="50%">
</h1>

# Pyggle
Web Demo: [Coming Soon!](url)

Find all possible words given a board and words, with a visual representation of the algorithm!
Check `lib/docs` for package details. For an example on how to use pyggle, check `lib/examples/example.py`!

## Tech Stack
[![JAVASCRIPT](https://img.shields.io/badge/typescript-3178C6?style=for-the-badge&logo=typescript&logoColor=FFF)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![NEXT.JS](https://img.shields.io/badge/NEXT-0769AD?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![TAILWINDCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/) \
The frontend is developed using `TypeScript` and the Next.js framework, with Tailwind CSS as the chosen `CSS` framework.

[![PYTHON](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FLASK](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/3.0.x/)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) \
The backend framework chosen for this project is Flask, a `Python`-based framework. In Flask, I create API endpoints to communicate with the frontend (the client).
These endpoints are designed to decipher the given boggle board from the client and return all possible combinations, coordinates, and score. 
The user can also send an image of a boggle board.

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

# this is only 3000 words, but the web demo will all utilize 380k words
with open('sample_data.txt', 'r') as file:
  words = [line.strip() for line in file]

boggle = Boggle(board, words)

# print full dictionary
print(boggle.solver())

# print only words
print(boggle.get_words())

# print only coords
print(boggle.get_coords())

# print word: coord format
boggle.print_result()
```
