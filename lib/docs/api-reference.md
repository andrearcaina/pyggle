# Pyggle API Reference

## Class: Boggle

### Constructor

#### `__init__(board: List[List[str]], words: List[str])`

Initialize a Boggle game instance with the given board and word list.

- `board`: List of lists representing the Boggle game board.
- `words`: List of strings representing valid words for the Boggle game.

### Methods

#### `solver() -> Dict[str, List[Tuple[int, int]]]`

Solve the Boggle game and return a dictionary of words found on the board along with their positions.

- Returns: Dictionary where keys are words found on the board and values are lists of tuples representing the positions of the word on the board.

#### `get_words() -> List[str]`

Retrieve a list of words found on the board.

- Returns: List of strings representing words found on the Boggle board.

#### `get_coords() -> List[List[Tuple[int, int]]]`

Retrieve a list of coordinates for each word found on the board.

- Returns: List of lists where each inner list contains tuples representing the positions of a word on the Boggle board.

#### `print_result() -> None`

Print the results of the Boggle game, showing each word found and its corresponding positions.

- Output: Prints each word found on the Boggle board along with its positions.
