def genEmptyBoard(n):
    board = []
    for i in range(n):
        row = []
        for i in range(n):
            row.append("*")
        board.append(row)
    return board
def printBoard(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()
    return

if __name__ == "__main__":
    n = 5
    board = genEmptyBoard(n)
    printBoard(board)
    

