from lib import genEmptyBoard, printBoard

n = 5

board = genEmptyBoard(n)

for i in range(n):
    board[0][i] = "Q"

printBoard(board)