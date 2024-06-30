# Minesweeper-Python-Replica
Text-based replica of the game Minesweeper, made using Python

Run the Python program and use the terminal to communicate with the program Follow the instructions printed in the terminal

--- To-Do ---
- Implement auto-reveal for tiles next to the revealed zero tile
- The "ask..." functions could be made into one function, since the structure is so similar
- Revealing the board after the game is done

--- Program Structure ---

Structure of the main program goes as follows:
- Ask for user for input regarding dimensions of the board
- Initialize board with said dimensions, with a ratio of the spaces being landmines
- Execute the following until a win/lose condition is thrown
  - Ask user for the square to perform an action upon
  - Perform the action, checking whether that action leads to a win/lose condition
- When a win or lose condition is met, print out the corresponding message to win/lose

Structure of the classes:
- Main program works with a class called Board and Tile, with the Board being a 2D list of Tiles
- Board object keeps track of the state of the board, and only has a 2D list of Tiles and its dimensions
- Tile object keeps track of whether it is a mine, revealed, flagged, and also number of mines around this tile (unless it itself is a mine)
- Main program gets the traits of the Tiles through the Board object

--- Reflection ---
- In comparison to the Java program, this is more modularized, and uses better names
- I feel like using classes for both the Board and each Tile was a better implementation than what I used in the Java program
- Java program generates the value of the tile when it is revealed, while the Python program generates it on initialization of the board
  - Checking 8 tiles uses an insignificant amount of time, but regardless, Java is faster to initialize and doesn't waste time generating values for tiles that the user possibly won't reveal, while Python is faster at revealing the values inbetween moves (it is only a matter of showing the value, generation is done on initialization of the board)
