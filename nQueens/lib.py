# 生成二維矩陣的棋盤
def genEmptyBoard(n):
    board = []
    for i in range(n):
        row = []
        for i in range(n):
            row.append("*")
        board.append(row)
    return board
# 顯示二維矩陣的棋盤
def printBoard(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()
        
    return

