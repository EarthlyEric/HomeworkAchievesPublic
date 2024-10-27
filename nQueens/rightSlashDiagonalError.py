from lib import genEmptyBoard, printBoard

n = 5

board = genEmptyBoard(n)

for i in range(n):
    board[(n-1)-i][i] = "Q"

printBoard(board)