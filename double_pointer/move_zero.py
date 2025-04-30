'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]


提示:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


进阶：你能尽量减少完成的操作次数吗？
'''
import math
from math import floor
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)
        zeroCount = 0
        for i in range(length):
            if nums[i] == 0:
                zeroCount+=1
            elif zeroCount > 0 and[i] != 0:
                nums[i-zeroCount] = nums[i]
                nums[i] = 0


if __name__ == '__main__':
    solution = Solution()
    case1 = [
        [0,1,0,3,12],[0],[1,5,7,0,3],
        [0,0,1]]
    case2 = [
        [1,3,12,0,0],[0],[1,5,7,3,0],
        [1,0,0]]
    res = []
    for i in range(len(case1)):
        solution.moveZeroes(case1[i])
        print(f'expect: {case2[i]}, res: {case1[i]}')
        # res.append(r)
    print(res)
