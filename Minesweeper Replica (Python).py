import Board

class WinCondition(Exception):
    pass

class LoseCondition(Exception):
    pass

def ask_value(dimension):
    height = int(input("Set " + dimension + " of the board: "))
    while height <= 0:
        height = int(input("Invalid input. Please enter a positive integer as value for " + dimension + ": "))
    return height

def ask_place(max_width, max_height):
    x = int(input("Set the x-coordinate of the tile (starts with 1): "))
    while x <= 0 or x > max_width:
        x = int(input("Invalid input. Please enter a value between 1 and " + str(max_width) + ": "))
    y = int(input("Set the y-coordinate of the tile (starts with 1): "))
    while y <= 0 or y > max_height:
        y = int(input("Invalid input. Please enter a value between 1 and " + str(max_height) + ": "))
    return x - 1, y - 1
    
def ask_action() -> str:
    action = str(input("Choose an action: flag/unflag/reveal: "))
    while action != "flag" and action != "unflag" and action != "reveal":
        action = str(input("Invalid action. Please enter 'flag', 'unflag', or 'reveal' as the action: "))
    return action

if __name__ == "__main__":
    width = ask_value("width")
    height = ask_value("height")
    minesweeper_board = Board.Board(width, height, width*height // 5)
    try:
        while True:
            print(minesweeper_board)
            
            x, y = ask_place(width, height)
            action = ask_action()
            if (action == "flag" or action == "unflag"):
                minesweeper_board.get_tile(x, y).flag()
            elif (action == "reveal"):
                if minesweeper_board.get_tile(x, y).is_revealed():
                    print("This tile is already revealed.")
                else:
                    if minesweeper_board.reveal_tile(x, y): # If the tile is a mine, raise LoseCondition
                        raise LoseCondition

            if (minesweeper_board.get_num_revealed() == width*height - width*height // 5):
                raise WinCondition
            
    except WinCondition:
        print("\nYou win!")
    except LoseCondition:
        print("\nYou lost!")