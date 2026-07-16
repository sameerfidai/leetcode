# Time:   O(N)
# Space:  O(N)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [index, d[diff]]
            else:
                d[num] = index
