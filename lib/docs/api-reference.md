# Pyggle API Reference

## Class: Boggle

### Constructor

#### `__init__(board: List[List[str]], words: List[str], official: bool = False)`

Initialize a Boggle game instance with the given board, word list, and official status.

- `board`: List of lists representing the Boggle game board or a string representing a single row of the board.
- `words`: List of strings representing valid words for the Boggle game.
- `official`: Boolean indicating whether to enforce official Boggle rules (default is `False`).

### Methods

#### `solver() -> Dict[str, List[Tuple[int, int]]]`

Solve the Boggle game and return a dictionary of words found on the board along with their positions.

- Returns: Dictionary where keys are words found on the board and values are lists of tuples representing the positions of the word on the board.

#### `get_length() -> int`

Calculate and retrieve the total length of the boggle board.

#### `get_words() -> List[str]`

Retrieve a list of words found on the board.

- Returns: List of strings representing words found on the Boggle board.

#### `get_coords() -> List[List[Tuple[int, int]]]`

Retrieve a list of coordinates for each word found on the board.

- Returns: List of lists where each inner list contains tuples representing the positions of a word on the Boggle board.

#### `get_score() -> List[int]`

Calculate and retrieve the score for each word found on the board.

#### `time_solve() -> float`

Return how long it takes to solve the given boggle board and given list of words.

#### `print_result() -> None`

Print the results of the Boggle game, showing each word found and its corresponding positions.

- Output: Prints each word found on the Boggle board along with its positions.

- Returns: List of integers representing the score for each word found.

#### `print_board() -> None`

Print the board of the Boggle game, showing each letter as a visual representation.

- Output: Prints each letter on the terminal as an N x M matrix.

### Private Methods

#### `__bogglefy()`

Private method to convert a string representation of the board into a list of lists.

#### `__stringify()`

Private method to convert the board into a string representation. Used in conjunction with `print_board()`.

#### `__check_board()`

Private method to check if the board is valid.

#### `__check_words()`

Private method to check if the words are valid.

#### `__check_official()`

Private method to check if the official status is valid.

#### `__algorithm()`

Private method to call the algorithm for `solver()`.

#### `__search()`

Private method that performs DFS on the boggle board. Used in conjunction with `__algorithm()`.

#### `__filter()`

Private method that filters the words in the list of words dependent on `self.official`.

### Dunder Methods

#### `__print__()`

Special method that prints the given board as a string. Used in conjunction with `print_board()`.

#### `__str__()`

Special method that prints the does the same thing as `__stringify()`.

#### `__getitem__()`

Special method that allows you to access elements of the boggle board from the object.

#### `__contains__()`

Special method that allows you to check if the solutions from the boggle board contains a specific word.
