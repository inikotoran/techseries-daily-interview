# A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k,
# we want to figure out after k random moves by a knight,
# the probability that the knight will still be on the chessboard.
# Once the knight leaves the board it cannot move again and will be considered off the board.

# Notes:
# Grid: 8x8
# Possible moves = 8
# origin (x, y)
# move1 (x+2, y+1)
# move2 (x+2, y-1)
# move3 (x-2, y+1)
# move4 (x-2, y-1)
# move5 (x+1, y+2)
# move6 (x+1, y-2)
# move7 (x-1, y+2)
# move8 (x-1, y-2)

def is_knight_on_board(x, y, k, cache={}):
    # Fill this in.
    if x > 7 or x < 0 or y > 7 or y < 0:
      return 0
    if k == 0:
      return 1
    return (0.0
      + is_knight_on_board(x+2, y+1, k-1)
      + is_knight_on_board(x+2, y-1, k-1)
      + is_knight_on_board(x-2, y+1, k-1)
      + is_knight_on_board(x-2, y-1, k-1)
      + is_knight_on_board(x+1, y+2, k-1)
      + is_knight_on_board(x+1, y-2, k-1)
      + is_knight_on_board(x-1, y+2, k-1)
      + is_knight_on_board(x-1, y-2, k-1)) / 8


print(is_knight_on_board(0, 0, 1))
# 0.25
