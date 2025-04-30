from math import floor
from re import search


def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_index = floor(left + (right - left) / 2)
        mid = nums[mid_index]

        if mid == target:
            return mid_index
        elif mid < target:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return -1

if __name__ == '__main__':

    nums = [10, 20, 30, 40, 50]
    print(binary_search(nums, 30))  # 应该返回 2
    print(binary_search(nums, 25))  # 应该返回 -1

