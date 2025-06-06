from math import floor
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = floor(left + (right - left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    case1 = [([-1,0,3,5,9,12],9),([-1,0,3,5,9,12],2),([0,3,5,6,8],5),([0,3,5,6,8],0)]
    answer = [4, -1, 2, 0]
    res = []
    for i in range(len(case1)):
        case = case1[i]
        r = solution.search(case[0],case[1])
        print(f'sub: {case1[i]}, target: {answer[i]}, res: {r}')
        res.append(r)
    print(res)


'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1


提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。

'''