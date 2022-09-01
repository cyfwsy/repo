"使用深度優先算法，解決八皇后問題"
ANSWER_COUNT = 0
MAXNUM = 8

# 检查当前坐标是否能放置queen
# 只需检查当前坐标的↖↑↗这三个坐标上侧方向
# 因为本行的落子不受下一行的影响
# 所以无需检查←↙↓↘→这5个与坐标同行或坐标下侧的方向
def check(x,y,chess):
    for i in range(x):
        # 检查竖向↑（只需检查当前行之上的行）
        if(chess[i][y]==1):
            return False    

        # 检查左上斜方向↖
        if(y-1-i >= 0):
            if(chess[x-1-i][y-1-i] == 1):
                return False

        # 检查右上斜方向↗
        if(y+1+i < MAXNUM):
            if(chess[x-1-i][y+1+i] == 1):
                return False

    return True

# 打印棋盘
def print_chess(chess):
    print('answer {}:'.format(ANSWER_COUNT))
    for i in range(MAXNUM):
        for j in range(MAXNUM):
            print(chess[i][j],' ',end='')
        print('\n')
    print('\n')

# 递归求解8个queen的放置方式
def find_queen8(x,chess):
    global ANSWER_COUNT,MAXNUM

    # 临时棋盘，复制上一行的queen皇后落子后的棋盘
    chess_temp = [[0 for col in range(MAXNUM)] for row in range(MAXNUM)]
    for i in range(MAXNUM):
        for j in range(MAXNUM):
            chess_temp[i][j] = chess[i][j]

    # x等于棋盘边界，代表已最后一行的queen已经落子，打印结果并返回
    if(x == MAXNUM):
        ANSWER_COUNT = ANSWER_COUNT + 1
        print_chess(chess_temp)
        return

    # 遍历当前行的每一列
    for i in range(MAXNUM):

        # 判断当前点能否放置queen
        if(check(x,i,chess_temp)):

            # 能放置，置为1，以供打印棋盘
            chess_temp[x][i] = 1

            # 寻找下一行queen的落点
            find_queen8(x+1,chess_temp)

            # 本列的深度搜索结束
            # 将本列的点置为0，然后遍历下一列
            chess_temp[x][i] = 0

def main():
    #初始棋盘
    chess = [[0 for col in range(MAXNUM)] for row in range(MAXNUM)]

    #从第0行开始
    find_queen8(0,chess)

    #打印结果
    print('求解{}皇后问题，共有{}个答案: '.format(MAXNUM, ANSWER_COUNT))

if __name__ == '__main__':
    main()