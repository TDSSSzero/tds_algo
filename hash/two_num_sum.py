'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
'''
from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     index_list = []
    #     for i in range(len(nums)):
    #         index_list.append(i)
    #         for j in range(i + 1, len(nums)):
    #             if nums[j] == target - nums[index_list[0]]:
    #                 index_list.append(j)
    #                 return index_list
    #         index_list.clear()
    #     return index_list

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for i,num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num],i]
            hash_table[nums[i]] = i
        return []


if __name__ == '__main__':
    solution = Solution()
    case1 = [
        # ([2,7,11,15],9),([3,2,4],6),([3,3],6),([2,3,7,11,15],9),
        #      ([0,4,3,0],0)
        ([-1, -2, -3, -4, -5],-8)
    ]
    case2 = [
        # [0,1],[1,2],[0,1],[0,2],
        #      [0,3]
        [2,4]
    ]
    res = []
    for i in range(len(case1)):
        r = solution.twoSum(case1[i][0],case1[i][1])
        print(f'expect: {case2[i]}, res: {r}')
        res.append(r)
    print(res)
