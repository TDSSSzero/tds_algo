'''
你在一家生产小球的玩具厂工作，有 n 个小球，编号从 lowLimit 开始，到 highLimit 结束（包括 lowLimit 和 highLimit ，即 n == highLimit - lowLimit + 1）。另有无限数量的盒子，编号从 1 到 infinity 。

你的工作是将每个小球放入盒子中，其中盒子的编号应当等于小球编号上每位数字的和。例如，编号 321 的小球应当放入编号 3 + 2 + 1 = 6 的盒子，而编号 10 的小球应当放入编号 1 + 0 = 1 的盒子。

给你两个整数 lowLimit 和 highLimit ，返回放有最多小球的盒子中的小球数量。如果有多个盒子都满足放有最多小球，只需返回其中任一盒子的小球数量。
'''


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        map = {}
        for i in range(lowLimit,highLimit + 1):
            s = str(i)
            boxNum = 0
            for c in s:
                boxNum += int(c)
            if map.__contains__(boxNum):
                map[boxNum] += 1
            else:
                map[boxNum] = 1
        return max(map.values())


if __name__ == '__main__':
    solution = Solution()
    case1 = [(1,10),(5,15),(19,28)]
    case2 = [2,2,2]
    res = []
    for i in range(len(case1)):
        r = solution.countBalls(case1[i][0],case1[i][1])
        print(f'expect: {case1[i]}, res: {case2[i]}')
        res.append(r)
    print(res)