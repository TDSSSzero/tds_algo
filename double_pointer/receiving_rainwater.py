from typing import List

class Solution:

    def trap_double_point(self, height: List[int]) -> int:
        l = len(height)
        if l == 0:
            return 0
        count = left = 0
        right = l - 1
        l_max = height[0]
        r_max = height[l - 1]
        while left < right:
            l_max = max(l_max,height[left])
            r_max = max(r_max,height[right])
            if l_max < r_max:
                count += l_max - height[left]
                left += 1
            else:
                count += r_max - height[right]
                right -= 1
        return count

    def trap_note(self, height: List[int]) -> int:
        l = len(height)
        l_max = [0] * l
        l_max[0] = height[0]
        r_max = [0] * l
        r_max[l - 1] = height[l - 1]

        for i in range(1,l):
            l_max[i] = max(height[i],l_max[i-1])
        for i in range(l-2,0,-1):
            r_max[i] = max(height[i],r_max[i+1])

        count = 0
        for i in range(1,l - 1):
            water = min(l_max[i], r_max[i]) - height[i]
            if water > 0:
                count += water
        return count

    def trap(self, height: List[int]) -> int:
        l = len(height)
        count = 0
        for i in range(1,l - 1):
            left_max = 0
            for left_index in range(0, i):
                left_max = max(height[left_index], left_max)
            right_max = 0
            for right_index in range(i, l):
                right_max = max(height[right_index], right_max)
            water = min(left_max, right_max) - height[i]
            if water > 0:
                count += water
        return count


if __name__ == '__main__':
    solution = Solution()
    case1 = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5]
    ]
    answer = [
        6,
        9
    ]
    res = []
    for i in range(len(case1)):
        case = case1[i]
        r = solution.trap_double_point(case)
        print(f'sub: {case1[i]}, target: {answer[i]}, res: {r}')
        res.append(r)
    print(res)




'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）
。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
'''