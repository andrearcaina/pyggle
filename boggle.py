class Boggle:
    def __init__(self, board, words):
        self.board = board
        self.words = words

    def solver(self):
        result = {}
        rows = len(self.board)
        cols = len(self.board[0])
        length = rows * cols

        for word in self.words:
            positions = []
            if len(word) <= length:
                for i in range(rows):
                    for j in range(cols):
                        if self.board[i][j] == word[0] and word not in result:
                            if self.search(word, i, j, rows, cols, positions):
                                result[word] = positions
        return result

    def search(self, word, x, y, rows, cols, positions):
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
                if self.search(word[1:], x + i, y + j, rows, cols, positions):
                    return True

        positions.pop()
        return False
    
    def print(self):
        result = self.solver()

        for word, positions in result.items():
            print(word+":", positions)
        
if __name__ == '__main__':    
    board = [['e', 'a'], ['s', 't']]
    words = [line.strip() for line in open('files/word_list_3000.txt', 'r')]
    boggle = Boggle(board, words)
    boggle.print()