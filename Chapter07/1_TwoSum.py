# 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스 반환

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx, n in enumerate(nums):
            res = target - n
            if res in nums[idx + 1:]:
                return [nums.index(n), nums[idx + 1:].index(res) + (idx + 1)]
            
        
            

sol = Solution()
nums = [3, 2, 3]
target = 6
print(sol.twoSum(nums, target))
