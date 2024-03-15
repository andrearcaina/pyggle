import os
from typing import Union
from timeit import timeit

class Boggle:
    def __init__(self, board: Union[list[list[str]], str], words: list[str] = [], official: bool = False):
        self.board = board
        self.words = words
        self.official = official

        if not self.words:
            this_directory = os.path.abspath(os.path.dirname(__file__))
            words_alpha_path = os.path.join(this_directory, "data", "words_alpha.txt")
            
            with open(words_alpha_path, "r") as f:
                self.words = [word.strip() for word in f]

        if self.__check_board():
            raise TypeError("Board must be a list of lists or string")
        
        if self.__check_words():
            raise TypeError("Words must be a list of strings")
        
        if self.__check_official():
            raise TypeError("Official must be a boolean")

        if isinstance(self.board, str):
            self.board = self.__bogglefy()

    def __print__(self) -> None:
        self.print_board()

    def __str__(self) -> str:
        return self.__stringify()

    def __len__(self) -> int:
        return self.get_length()

    def __repr__(self) -> str:
        return f"Boggle({self.board}, {self.words}, {self.official})"

    def __getitem__(self, x: int) -> str:
        if isinstance(x, int) and 0 <= x < self.get_length():
            return self.board[x]
        raise IndexError("Index out of range")

    def __contains__(self, word: str) -> bool:
        return word in self.get_words()
    
    def solver(self) -> dict[str, list[tuple[int]]]:
        if self.official and self.get_length() < 3:
            return {}

        result = {}
        rows = len(self.board)
        cols = len(self.board[0])
        
        for word in self.__filter():
            positions = []
            self.__algorithm(word, positions, rows, cols, result)

        return result

    def get_length(self) -> int:
        return len(self.board) * len(self.board[0])

    def get_words(self) -> list:
        if not self.solver():
            return []

        return [key for key in self.solver().keys()]

    def get_coords(self) -> list:
        if not self.solver():
            return []

        return [value for value in self.solver().values()]

    def get_score(self) -> list[int]:
        score = []
        words = self.get_words()
        word_scores = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5}

        if not words:
            return []

        for word in words:
            word_length = len(word)
            if word_length in word_scores:
                score.append(word_scores[word_length])
            else:
                score.append(11)

        return score

    def time_solve(self) -> float:
        return timeit(self.solver, number=1)

    def print_result(self) -> None:
        if not self.solver():
            print("No words!")
            return

        result = self.solver()

        for word, positions in result.items():
            print(f"{word}: {positions}")

    def print_board(self) -> None:
        print(self.__stringify())

    def __check_board(self) -> bool:
        sublist_type = all(isinstance(sublist, list) for sublist in self.board)

        return not (isinstance(self.board, list) and sublist_type) and not isinstance(self.board, str)

    def __check_words(self) -> bool:
        return not isinstance(self.words, list)
    
    def __check_official(self) -> bool:
        return not isinstance(self.official, bool)

    def __bogglefy(self) -> list[list[int]]:
        return [list(row) for row in self.board.split()]
    
    def __stringify(self) -> str:
        return "\n".join([" ".join(row) for row in self.board])

    def __filter(self) -> list:
        if not self.official:
            return [word for word in self.words if len(word) <= self.get_length()]
        return [word for word in self.words if len(word) >= 3 and len(word) <= self.get_length()]

    def __algorithm(self, word: str, positions: list, rows: int, cols: int, result: dict) -> None:
        for i in range(rows):
            for j in range(cols):
                if self.board[i][j] == word[0] and word not in result:
                    if self.__search(word, i, j, rows, cols, positions):
                        result[word] = positions

    def __search(self, word: str, x: int, y: int, rows: int, cols: int, positions: list) -> bool:
        if (x, y) in positions:
            return False
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        if self.board[x][y] != word[0]:
            return False

        positions.append((x, y))

        if len(word) == 1:
            return True

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                move = self.__search(word[1:], x + i, y + j, rows, cols, positions)
                
                if move:
                    return True

        positions.pop()
        return False
