import os

class Boggle:
    def __init__(self, board, words=None, official=False):
        self.board = board
        self.words = words
        self.official = official

        if self.__check_board():
            raise TypeError("Board must be a list of lists or string")
        
        if self.__check_words():
            raise TypeError("Words must be a list of strings")
        
        if self.__check_official():
            raise TypeError("Official must be a boolean")

        if isinstance(self.board, str):
            self.board = self.__bogglefy()

        if not self.words:
            this_directory = os.path.abspath(os.path.dirname(__file__))
            words_alpha_path = os.path.join(this_directory, "data", "words_alpha.txt")
            
            with open(words_alpha_path, "r") as f:
                self.words = [word.strip() for word in f]

    def __bogglefy(self):
        return [list(row) for row in self.board.split()]

    def __check_board(self):
        sublist_type = all(isinstance(sublist, list) for sublist in self.board)

        return not (isinstance(self.board, list) and sublist_type) and not isinstance(self.board, str)

    def __check_words(self):
        return not isinstance(self.words, list)
    
    def __check_official(self):
        return not isinstance(self.official, bool)

    def solver(self):
        if self.official and self.get_length() < 3:
            return None

        result = {}
        rows = len(self.board)
        cols = len(self.board[0])
        length = rows * cols

        for word in self.words:
            positions = []
            if not self.official:
                if len(word) <= length:
                    self.__algorithm(word, positions, rows, cols, result)
            else:
                if len(word) >= 3 and len(word) <= length:
                    self.__algorithm(word, positions, rows, cols, result)

        return result

    def __algorithm(self, word, positions, rows, cols, result):
        for i in range(rows):
            for j in range(cols):
                if self.board[i][j] == word[0] and word not in result:
                    if self.__search(word, i, j, rows, cols, positions):
                        result[word] = positions


    def __search(self, word, x, y, rows, cols, positions):
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

    def get_length(self):
        return len([char for sublist in self.board for char in sublist])

    def get_words(self):
        if not self.solver():
            return None

        return [key for key in self.solver().keys()]

    def get_coords(self):
        if not self.solver():
            return None

        return [value for value in self.solver().values()]

    def get_score(self):
        score = []
        words = self.get_words()
        word_scores = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5}

        for word in words:
            word_length = len(word)
            if word_length in word_scores:
                score.append(word_scores[word_length])
            else:
                score.append(11)

        return score

    def print_result(self):
        if not self.solver():
            print("No words!")
            return

        result = self.solver()

        for word, positions in result.items():
            print("{}: {}".format(word, positions))
