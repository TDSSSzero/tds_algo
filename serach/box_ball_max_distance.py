from typing import List
'''
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。
Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。

已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。

给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。
'''

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = position[-1] - position[0]
        while left <= right:
            mid = (left + right) // 2
            if self.can_place(position,m,mid):
                left = mid + 1
            else:
                right = mid - 1
        return right

    def can_place(self,position,m,distance) -> bool:
        count = 1
        last_place = position[0]
        for pos in position[1:]:
            if pos - last_place >= distance:
                count += 1
                last_place = pos
            if count >= m:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    case1 = [([1,2,3,4,7],3),([5,4,3,2,1,1000000000],2),([1,10,6,15,22],4),([1,2,3,4,7],4)]
    case2 = [3,999999999,3,5,1]
    res = []
    for i in range(len(case1)):
        r = solution.maxDistance(case1[i][0],case1[i][1])
        print(f'input: {case1[i]}, expect: {case2[i]}')
        res.append(r)
    print(res)