2-D Cellular automata engine which is (somewhat) general to update rule and
neighborhood

This is not working yet.

To use 2cell, define a rule function which manipulates a chunk of a NumPy array
and initialize a new CA type with it, and then call `CA.run()`:
``` python
def game_of_life(data):
    self = data[1, 1]
    neighbors = data[0, 0] + data[0, 1] + data[0, 2] + \
                data[1, 0] +              data[1, 2] + \
                data[2, 0] + data[2, 1] + data[2, 2]

    if self:
        if neighbors < 2 or neighbors > 3:
            return 0
    elif neighbors == 3:
        return 1
    return 0

# initialize a board to a game-of-life glider
board = np.zeros((100,100), dtype=np.uint8)
board[3,2] = 255
board[4,2] = 255
board[5,2] = 255
board[5,2] = 255
board[4,2] = 255

ca = CA(board, game_of_life)

ca.run()
```

2cell uses NumPy to represent the automaton board, and PyGame to render it.
