import random

class Board:
    def __init__(self, width: int, height: int, num_mines: int):
        # Initialization of the board
        self._board = self._fill_array(width, height)
        self._width, self._height = width, height
        self._revealed = 0
        current_mines = 0
        # Randomly selects tiles to be mines
        while current_mines < num_mines:
            random_x = random.randint(0, width - 1)
            random_y = random.randint(0, height - 1)
            random_tile = self._board[random_y][random_x]
            print("Try setting mine: (" + str(random_x) + ", " + str(random_y) + ") " + str(random_tile.is_mine()))
            if not random_tile.is_mine():
                random_tile._set_mine()
                self._increment_surrounding(random_x, random_y)
                current_mines += 1
    
    def __repr__(self):
        current_string = ""
        for r in range(self._height):
            for c in range(self._width):
                current_string += str(self._board[r][c])
            current_string += "\n"
        return current_string
    
    def reveal_tile(self, x: int, y: int) -> bool:
        if self._board[y][x]._reveal():
            return True
        else:
            if self._board[y][x].get_num() == 0:
                for potential_x in range(max(x - 1, 0), min(x + 1, self._width - 1) + 1):
                    for potential_y in range(max(y - 1, 0), min(y + 1, self._height - 1) + 1):
                        if not self._board[potential_y][potential_x].is_revealed():
                            self.reveal_tile(potential_x, potential_y)
            self._revealed += 1
            return False

    def reveal_all(self):
        for r in range(self._height):
            for c in range(self._width):
                if not self._board[r][c].is_revealed():
                    self._board[r][c]._reveal()

    def get_tile(self, x: int, y: int) -> "Tile":
        return self._board[y][x]
    
    def get_num_revealed(self) -> int:
        return self._revealed

    def _increment_surrounding(self, x: int, y: int):
        # For each adjacent tile (accounting for edges)
        for potential_x in range(max(x - 1, 0), min(x + 1, self._width - 1) + 1): 
            for potential_y in range(max(y - 1, 0), min(y + 1, self._height - 1) + 1): 
                if (potential_x != x or potential_y != y): # If it is not the current tile
                    self._board[potential_y][potential_x]._increment_num()

    def _fill_array(self, width: int, height: int) -> list:
        empty_board = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(Tile())
            empty_board.append(row)
        return empty_board

class Tile:
    def __init__(self):
        self._is_mine = False
        self._is_revealed = False
        self._is_flagged = False
        self._num = 0

    def __repr__(self):
        if self._is_revealed:
            return "[" + str(self._num) + "]"
        elif self._is_flagged:
            return "[P]"
        else:
            return "[ ]"

    def _increment_num(self):
        if (self._num != 9):
            self._num += 1
    
    def _reveal(self) -> bool:
        self._is_revealed = True
        return self.is_mine()
    
    def flag(self) -> bool:
        # Reverses the state of the flag on this tile
        self._is_flagged = not self._is_flagged

    def _set_mine(self):
        self._is_mine = True
        self._num = 9
    
    def is_mine(self) -> bool:
        return self._is_mine
    
    def is_revealed(self) -> bool:
        return self._is_revealed
    
    def get_num(self) -> bool:
        return self._num
