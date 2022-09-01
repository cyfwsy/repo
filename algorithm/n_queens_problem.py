class solution(object):
    """ N queen problem,
    初始化一个列表columnPosition=[-1]*8, 其中的每一个值表示每一行皇后所在位置的索引值。\
        解决此问题,columnPosition需满足两个条件:
        1)列表中不能出项重复元素。
        2)abs(columnPosition[i]-columnPosition[j]) == int(j-i)\
        即 对角线上不能出现重复元素。"""

    def __init__(self):
        self._count = 0

    def solveNQueens(self, n):
        self.helper([-1]*n, 0, n)
        print('number of solution-------------->',self._count)

    def helper(self, columnPosition, rowindex, n):  # ding
        # print(rowindex)
        if rowindex == n:
            self.printSolution(columnPosition, n)
            # print(columnPosition)
            self._count += 1
            return
        # for column in range(n-rowindex):
        for column in range(n):
            columnPosition[rowindex] = column
            if self.isValid(columnPosition, rowindex):
                self.helper(columnPosition, rowindex+1, n)

    def isValid(self, columnPosition, rowindex):
        if len(set(columnPosition[:rowindex+1])) != len(columnPosition[:rowindex+1]):
            # print(columnPosition, rowindex)
            return False
        for i in range(rowindex):
            if abs(columnPosition[i]-columnPosition[rowindex]) == int(rowindex-i):
                # print(columnPosition, rowindex)
                return False
        return True

    def printSolution(self, columnPosition, n):
        # print(columnPosition)
        for row in range(n):
            line = ""
            for column in range(n):
                if columnPosition[row] == column:
                    line += "Q\t"
                else:
                    line += ".\t"
            print(line, "\n")
        print('\n')


s = solution()
s.solveNQueens(10)
