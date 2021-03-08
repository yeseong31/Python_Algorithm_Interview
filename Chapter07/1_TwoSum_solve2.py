# 두 수의 합 - in을 이용한 탐색

# 모든 조합을 비교하지 않고, 정답, 즉 타겟에서 첫 번째 값을 뺀 값
# target - n이 존재하는지 탐색

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            comp = target - n
            if comp in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(comp) + (i + 1)]

# runtime: 48 ms
# O(n^2)이지만 브루토 포스 풀이보다 in 연산 쪽이 훨씬 더 가볍고 빠르다.
