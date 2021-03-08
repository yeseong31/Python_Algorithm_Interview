# 두 수의 합 - 조회 구조 개선

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target - n]:
                return [nums_map[target - n], i]
            nums_map[n] = i

# runtime: 48 ms
