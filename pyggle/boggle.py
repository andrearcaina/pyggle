import os
from typing import Union
from timeit import timeit

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_word = True
        node.word = word

    def search(self, word: str) -> bool:
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True

class Boggle:
    def __init__(self, board: Union[list[list[str]], str], words: list[str] = None, official: bool = False):
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
            
        self.trie = Trie()
        for word in self.words:
            self.trie.insert(word.lower())

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
    
    def solve(self) -> dict[str, list[tuple[int, int]]]:
        return self.solve_trie()

    def solve_dfs(self) -> dict[str, list[tuple[int, int]]]:
        if self.official and self.get_length() < 3:
            return {}

        result = {}
        rows = len(self.board)
        cols = len(self.board[0])
        
        for word in self.words:
            self.__filter(word, [], rows, cols, result)

        return result

    def solve_trie(self) -> dict[str, list[tuple[int, int]]]:
        if self.official and self.get_length() < 3:
            return {}

        result = {}
        rows = len(self.board)
        cols = len(self.board[0])
        
        for i in range(rows):
            for j in range(cols):
                visited = [[False] * cols for _ in range(rows)]
                self.__dfs_trie(i, j, rows, cols, "", self.trie.root, visited, [], result)
        
        return result

    def get_length(self) -> int:
        return len(self.board) * len(self.board[0])

    def get_words(self) -> list[str]:
        if not self.solve():
            return []

        return [key for key in self.solve().keys()]

    def get_coords(self) -> list[tuple[int, int]]:
        if not self.solve():
            return []

        return [value for value in self.solve().values()]

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
        return timeit(self.solve, number=1)

    def time_solve_trie(self) -> float:
        return timeit(self.solve_trie, number=1)

    def time_solve_dfs(self) -> float:
        return timeit(self.solve_dfs, number=1)

    def print_result(self) -> None:
        if not self.solve():
            print("No words!")
            return

        for word, positions in self.solve().items():
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

    def __filter(self, word: str, positions: list, rows: int, cols: int, result: dict) -> None:
        if not self.official:
            if len(word) <= self.get_length():
                self.__algorithm(word, positions, rows, cols, result)
        else:
            if len(word) >= 3 and len(word) <= self.get_length():
                self.__algorithm(word, positions, rows, cols, result)

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
        
        if self.official:
            if word.startswith('qu'):
                return self.__traverse_directions(word[2:], x, y, rows, cols, positions)
            elif word[0] == 'q':
                return False

        if len(word) == 1:
            return True

        return self.__traverse_directions(word[1:], x, y, rows, cols, positions)

    def __traverse_directions(self, word: str, x: int, y: int, rows: int, cols: int, positions: list) -> bool:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue # skip current position when i = j = 0
                if self.__search(word, x + i, y + j, rows, cols, positions):
                    return True

        positions.pop()
        return False

    def __dfs_trie(self, x: int, y: int, rows: int, cols: int, current_word: str, node: TrieNode, visited: list[list[bool]], path: list[tuple[int, int]], result: dict) -> None:
        if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y]:
            return
        
        char = self.board[x][y].lower()
        
        if self.official and char == 'q':
            if 'qu' not in node.children:
                return
            node = node.children['qu']
            current_word += 'qu'
        else:
            if char not in node.children:
                return
            node = node.children[char]
            current_word += char
        
        visited[x][y] = True
        path.append((x, y))
        
        if node.is_word:
            if self.official:
                if len(current_word) >= 3:
                    if current_word not in result:
                        result[current_word] = path.copy()
            else:
                if current_word not in result:
                    result[current_word] = path.copy()
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                self.__dfs_trie(x + dx, y + dy, rows, cols, current_word, node, visited, path, result)
        
        visited[x][y] = False
        path.pop()
