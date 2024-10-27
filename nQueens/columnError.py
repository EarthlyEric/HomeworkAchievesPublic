from lib import genEmptyBoard, printBoard

n = 5

board = genEmptyBoard(n)

for i in range(n):
    board[i][0] = "Q"

printBoard(board)