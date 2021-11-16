from abc import ABC, abstractmethod
from enum import Enum
import string as s
import re


class Color(Enum):
    BLACK = 'X'
    RED = 'O'


class Piece:
    def __init__(self, color: Color):
        self.color = color

    def __str__(self):
        return self.color.value


class Player:
    def __init__(self, color: Color, pieces: list):
        self.color = color
        # list of Piece obj.s w/ the player i.e. not on game board
        self.pieces = pieces

    def get_input(self) -> tuple[int, int]:
        adr = list(re.sub('\s', '', input(
            f"Player {self.color.value}'s turn: ")))
        return ord(adr[0].upper()) - 65, int(adr[1]) - 1 if all(len(adr) == 2, adr[0] in list(s.ascii_letters), adr[1] in range(1, 10)) else -1, -1


class Board(ABC):
    """abstract class of the gameboard"""

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # a nested list of Piece (empty cell = None)
        self.cells = [[None for j in range(cols)] for i in range(rows)]

    def __str__(self):

        def border(N):  # print the border between rows
            result = ' ' * 2
            for i in range(N * 4):
                result += '+' if i % 4 == 0 else '-'

            return result + '+\n'

        def row(n, N):  # print one row

            def cell(y, x):  # print one cell
                piece = self.cells[y][x]
                if piece is None:
                    return ' '
                else:
                    return piece.color.value

            result = f'{n+1} |'
            for i in range(N):
                result += f' {cell(n, i)} |'

            return result + '\n'

        result = ' ' * 4
        for i in range(self.cols):
            result += chr(i+65) + ' ' * 3  # print the alphabets
        result += '\n' + border(self.cols)
        for i in range(self.rows):
            result += row(i, self.cols) + border(self.cols)

        return result

    @abstractmethod
    def move():
        pass


class Gekitai(Board):
    def __init__(self, N: int = 6, P: int = 8, L: int = 3):
        super().__init__(N, N)
        self.P = P
        self.L = L
        self.players = Player(Color.BLACK, [Color.BLACK.value for i in range(P)]), Player(
            Color.RED, [Color.RED.value for i in range(P)])

    def is_move_valid(self, y: int, x: int) -> bool:
        return True if all(y in range(1, self.rows), x in range(1, self.cols), self.cells[y][x] is None) else False

    def move(self, piece: Piece, y: int, x: int):
        pass

    def piece_in_line(self, player: Player) -> bool:
        pass

    def game_over(self) -> bool:
        pass

    def __str__(self):
        result = super().__str__()
        for i in range(2):
            result += f'{self.players[i].color.value}: {self.players[i].pieces}\n'

        return result

    # GAME BEGINS HERE


if __name__ == '__main__':
    red = Piece(Color.RED)
    blk = Piece(Color.BLACK)
    a = Gekitai()
    a.cells = [[red, red, blk, None, None, None] for i in range(6)]

    print(a)
