def show():
    for i in range(len(queens)):
        for j in range(len(queens[i])):
            print(queens[i][j], end=" ")
        print()

def xyput(x, y):
    queens[x-1][y-1] = "Q"

def printRow(x):
    for i in range(n):
        queens[x][i] = "*"

def printColumn(y):
    for i in range(n):
        queens[i][y] = "*"

def rightDiagonal(x, y):
    for i in range(n):
        for j in range(n):
            if (i - x) == (j - y):
                queens[i][j] = "*"

def leftDiagonal(x, y):
    for i in range(n):
        for j in range(n):
            if (i + j) == (x + y):
                queens[i][j] = "*"

while True:
    n = int(input("請輸入N>=4值:"))
    if n >= 4:
        break
    else:
        print("請輸入大於3的數字")

queens = [["X" for i in range(n)] for k in range(n)]
show()

while True:
    x, y = map(int, input("請輸入x和y值,以空格分割,欲結束請輸入0 0:---").split())
    if x == y == 0:
        break
    if (x > n or x < 0) or (y > n or y < 0):
        print("請輸入正確數字")
        continue
    printRow(x-1)
    printColumn(y-1)
    rightDiagonal(x-1, y-1)
    leftDiagonal(x-1, y-1)
    xyput(x, y)
    show()

print("程式結束")