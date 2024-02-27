# Pyggle

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) [![boggle_test Actions Status](https://github.com/euanacampbell/boggle_solver/workflows/boggle_test/badge.svg)](https://github.com/euanacampbell/boggle_solver/actions)

GitHub: [https://github.com/andrearcaina/pyggle](https://github.com/andrearcaina/pyggle)

PyPi: [https://pypi.org/project/pyggle/](https://pypi.org/project/pyggle/)

Find all possible words given a board and words, with a visual representation of the algorithm!
Check `lib/docs` for package details. For an example on how to use pyggle, check `lib/examples/example.py`!

## Installation

```bash
pip install pyggle
```

## Usage
```python
from pyggle import Boggle

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
