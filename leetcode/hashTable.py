# **************************哈希表************************** #


# 1. 两数之和
class Solution:
    def twoSum(self, nums, target: int):
        for i, x in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if x + nums[j] == target:
                    return [i, j]