class Board:
    def __init__(self):
        self.board = [["" for _ in range(7)] for _ in range(6)]

    def place_disc(self, col, symbol):

        for i in range(5, -1, -1):
            if self.board[i][col] == "":
                self.board[i][col] = symbol
                return i

    def is_column_full(self, col):

        for i in range(6):
            if self.board[i][col] == "":
                return False
        return True

    def check_win(self, row, col, symbol):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            total = 1
            total += self.count_dir(row, col, dr, dc, symbol)
            total += self.count_dir(row, col, dr, dc, symbol)
            if total >= 4:
                return True

        return False

    def count_dir(self, r, c, dr, dc, symbol):
        total = 0
        r += dr
        c += dc
        while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == symbol:
            total += 1
            r += dr
            c += dc
        return total
