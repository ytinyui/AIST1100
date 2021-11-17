from abc import ABC, abstractmethod
from enum import Enum
import string as s
import re
# FIXME: COMPARE COLOR OF PIECES INSTEAD OF PIECE OBJECTS FIXME:


class Color(Enum):
    BLACK = 'X'
    RED = 'O'

    EMPTY = ' '  # empty cell
    OUT = None  # out of board


class Piece:
    def __init__(self, color: Color):
        self.color = color


class Player:
    def __init__(self, color: Color, pieces: list):
        self.color = color
        # list of Piece obj.s w/ the player i.e. not on game board
        self.pieces = pieces

    def get_input(self) -> tuple[int, int]:
        adr = list(re.sub('\s', '', input(
            f"Player {self.color.value}'s turn: ")))
        return (int(adr[1]) - 1, ord(adr[0].upper()) - 65) if len(adr) == 2 and adr[0] in list(s.ascii_letters) and adr[1].isnumeric() else (-1, -1)


class Board(ABC):
    """abstract class of the gameboard"""

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # a nested list of Piece (empty cell = Color.EMPTY)
        self.cells = [[Piece(Color.EMPTY) for j in range(cols)]
                      for i in range(rows)]

    def get_piece(self, y, x) -> Piece:
        return self.cells[y][x] if y in range(self.rows) and x in range(self.cols) else Piece(Color.OUT)

    def __str__(self):

        def border(N):  # print the border between rows
            result = ' ' * 2
            for i in range(N * 4):
                result += '+' if i % 4 == 0 else '-'

            return result + '+\n'

        def row(n, N):  # print one row

            def cell(y, x):  # print one cell
                piece = self.get_piece(y, x)
                return piece.color.value

            result = f'{n+1} |'
            for i in range(N):
                result += f' {cell(n, i)} |'

            return result + '\n'

        # print first row
        result = ' ' * 4
        for i in range(self.cols):
            result += chr(i+65) + ' ' * 3  # print the alphabets
        result += '\n' + border(self.cols)
        # print following rows
        for i in range(self.rows):
            result += row(i, self.cols) + border(self.cols)

        return result

    @ abstractmethod
    def move():
        pass


class Gekitai(Board):

    def __init__(self, N: int = 6, P: int = 8, L: int = 3):
        super().__init__(N, N)
        self.P = P
        self.L = L
        self.players = Player(Color.BLACK, [Piece(Color.BLACK) for i in range(P)]), Player(
            Color.RED, [Piece(Color.RED) for i in range(P)])
        self.winner = None

    def is_move_valid(self, y: int, x: int) -> bool:
        return True if self.get_piece(y, x).color == Color.EMPTY else False

    def move(self, piece: Piece, y: int, x: int):
        self.cells[y][x] = piece
        # repel surrounding pieces
        dir = [[(j, i) for j in (-1, 0, 1)] for i in (-1, 0, 1)]
        for i in range(3):
            for j in range(3):
                dir_ = dir[j][i]
                adj_piece = self.get_piece(y + dir_[0], x + dir_[1])
                adj_adj_piece = self.get_piece(
                    y + dir_[0] * 2, x + dir_[1] * 2)

                if adj_piece.color in (Color.BLACK, Color.RED) and adj_adj_piece.color in (Color.EMPTY, 0):
                    if adj_adj_piece == 0:
                        # if pushed out of the board -> return piece to player
                        if self.players[0].color == adj_piece.color:
                            self.players[0].pieces.append(adj_piece)
                        else:
                            self.players[1].pieces.append(adj_piece)
                    else:
                        self.cells[y + dir_[0] * 2][x +
                                                    dir_[1] * 2] = adj_piece
                    self.cells[y + dir_[0]][x + dir_[1]] = Piece(Color.EMPTY)

        return

    def piece_in_line(self, player: Player) -> bool:
        dir = [[(j, i) for j in (0, 1)] for i in (-1, 0, 1)]
        # search each cell
        for i in range(self.rows):
            for j in range(self.cols):

                if self.get_piece(i, j).color == player.color:
                    for u in dir:
                        for v in u:
                            if v == (0, 0):  # exception
                                continue
                            k = 1
                            while self.get_piece(i + v[0] * k, j + v[1] * k).color == player.color:
                                k += 1
                                if k == self.L:
                                    return True

        return False

    def win(self, player: Player):
        return True if len(player.pieces) == 0 or self.piece_in_line(player) else False

    def game_over(self) -> bool:
        return True if self.win(self.players[0]) or self.win(self.players[1]) else False

    def __str__(self):
        result = super().__str__()
        for i in range(2):
            result += f'{self.players[i].color.value}: {[x.color.value for x in self.players[i].pieces]}\n'

        return result

    def start(self):
        # GAME BEGINS HERE
        c = 1  # identifies and controls player's turn
        """
        red = Piece(Color.RED)
        blk = Piece(Color.BLACK)
        ety = Piece(Color.EMPTY)
        self.cells = [[ety, ety, ety, ety, ety, ety],
                      [ety, blk, blk, ety, ety, ety],
                      [ety, blk, ety, red, ety, ety],
                      [ety, ety, red, ety, red, ety],
                      [ety, ety, ety, ety, ety, ety],
                      [ety, ety, ety, ety, ety, ety]]
                      """

        while not self.game_over():
            c += 1
            c %= 2
            print(self)
            # player input
            while 1:
                a = self.players[c].get_input()
                if self.is_move_valid(*a):
                    break
                print("Invalid move!")
            # apply move
            self.players[c].pieces.pop()
            self.move(Piece(self.players[c].color), *a)

        if self.win(self.players[0]) == self.win(self.players[1]):
            self.winner = self.players[c]
        elif self.win(self.players[0]):
            self.winner = self.players[0]
        else:
            self.winner = self.players[1]
        print(f'Game over:\n{self}\nPlayer {self.winner.color.value} wins!')

        return


if __name__ == '__main__':
    Gekitai().start()
