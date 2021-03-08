# 두 수의 합 - 첫 번째 수를 뺀 결과 키 조회

# 타겟에서 첫 번째 수를 빼면 두 번째 수를 바로 알아낼 수 있다.
# 두 분째 수를 키로 하고 기존의 인덱스는 값으로 바꿔서 딕셔너리로 저장하면
# 나중에 두 번째 수를 키로 조회해서 정답을 찾아낼 수 있다.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, n  in enumerate(nums):
            nums_map[n] = i
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target - n]:
                return [nums.index(n), nums_map[target - n]]

# runtime: 44 ms
# 평균 O(1), 최악 O(n)
