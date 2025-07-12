<h1 align="center">
  <img src="assets/pyggle_logo - white.png" alt="logo" width="50%">
</h1>

# Pyggle

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

GitHub: [https://github.com/andrearcaina/pyggle](https://github.com/andrearcaina/pyggle)

PyPi: [https://pypi.org/project/pyggle/](https://pypi.org/project/pyggle/)

Find all possible words given a board and words, with a visual representation of the algorithm!
Check `lib/docs` for package details. For an example on how to use pyggle, check `lib/examples/example.py`!

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

- [`/examples/2x2_example.py`](https://github.com/andrearcaina/pyggle/tree/main/examples/2x2_example.py) for general functions and more specificity
- [`/examples/qu_example.py`](https://github.com/andrearcaina/pyggle/tree/main/examples/qu_example.py) for an example where the letter 'Q' represents 'Qu'
- [`/docs/boggle-api.md`](https://github.com/andrearcaina/pyggle/tree/main/docs/boggle-api.md) for an understanding of each method

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
