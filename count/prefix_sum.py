from typing import List

'''
计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，
包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        s = [0] * (len(nums) + 1)
        s[0] = 0
        for i in range(1,len(s)):
            s[i] = self.prefix_sum(i)
        self.s = s
        print(f"s: {s}")

    def prefix_sum(self,target: int) -> int:
        sum = 0
        for i in range(target):
            sum += self.nums[i]
        return sum

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]


if __name__ == '__main__':
    numArray = NumArray([-2,0,3,-5,2,-1,6])
    case1 = [(0,2),(2,5),(0,5)]
    case2 = [1,-1,-3]
    res = []
    for i in range(len(case1)):
        r = numArray.sumRange(case1[i][0],case1[i][1])
        print(f'input: {case1[i]}, expect: {case2[i]}')
        res.append(r)
    print(res)