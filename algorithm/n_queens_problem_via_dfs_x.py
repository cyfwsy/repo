import time

def show(queen,n):
    for i in range(0, n):
        print("(" + str(i + 1) + ", " + str(queen[i] + 1) + ")", end = " ")
    print("\n")

def isNotConfict(queen, row):   #判断是否冲突
    for i in range(0, row):
        if queen[i] == queen[row] or abs(i - row) == abs(queen[i] - queen[row]):
            return False
    return True

sum = 0                         #记录解法总数

def put_queen(queen, row,n):      #回溯法放置皇后
    if row == len(queen):       #如果到达最后一行，那么肯定得到一种新解法
        show(queen,n)             #输出皇后位置
        global sum
        sum += 1                #更新解法总数
        return sum
    for column in range(0, len(queen)):#循环判断每列是否可以放置皇后
        queen[row] = column
        if isNotConfict(queen, row):
            put_queen(queen, row + 1,n)

def main(n):
    queen = [None] * n
    start = time.time()
    put_queen(queen, 0,n)
    end = time.time()
    print("共耗时:\n" + str(end - start) + " s\n")
    print("一共有" + str(sum) + "种解法")


if __name__ == '__main__':
    main(10)