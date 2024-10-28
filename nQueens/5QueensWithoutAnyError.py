from lib import genEmptyBoard, printBoard

# 生成5x5的空棋盤
n = 5
board = genEmptyBoard(n)
# 記錄每行皇后的位置，-1 表示未放置
"""      ROW  0   1   2   3   4
positions = [-1, -1, -1, -1, -1]

"""
queenPositions = [-1] * n
# 紀錄當前列是否找到解
foundSolution = False

"""

從0 行開始放置皇后

Empty board example:
       0 1 2 3 4 Column
0    > * * * * * 
1      * * * * *
2      * * * * *
3      * * * * *
4      * * * * *
Row
"""

targetRow = 0

while targetRow >= 0 and not foundSolution:
    foundPosition = False
    
    for col in range(queenPositions[targetRow] + 1, n):
        isSafe = True
        for i in range(targetRow):
            # abs()取絕對值
            # 檢測是否有其他皇后在同一列或對角線上
            if queenPositions[i] == col or abs(queenPositions[i] - col) == abs(i - targetRow):
                isSafe = False
                break
        
        # 當前位置是合理的，紀錄放置皇后的位置positions在，放置皇后，，跳出迴圈
        if isSafe:
            queenPositions[targetRow] = col
            board[targetRow][col] = "Q"
            foundPosition = True
            break
    
    # 如果找到合適的位置，則檢查是否已經放置了最後一個皇后
    if foundPosition:
        if targetRow == n - 1:
            foundPosition = True
            break
        else:
            targetRow = targetRow + 1
            queenPositions[targetRow] = -1
    else:
        if not queenPositions[targetRow] == -1:
            board[targetRow][queenPositions[targetRow]] = "."
        queenPositions[targetRow] = -1
        targetRow = targetRow-1

printBoard(board)
