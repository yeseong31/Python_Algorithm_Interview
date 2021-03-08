# 두 수의 합 - 브루토 포스로 계산

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# runtime: 48 ms
# O(n^2)
