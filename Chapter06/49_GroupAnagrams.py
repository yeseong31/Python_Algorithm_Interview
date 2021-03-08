# 그룹 애너그램
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

# '애너그램'
# 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 키가 존재하지 않을 경우를 대비하여 defaultdict() 사용
        dic = defaultdict(list)
        for s in strs:
            # 문자열 내의 문자를 재정렬하여 그것을 키로 삼음
            dic[''.join(sorted(s))].append(s)
        return dic.values()

    
solution = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))
# [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
print(solution.groupAnagrams(strs))
# [[""]]

strs = ["a"]
print(solution.groupAnagrams(strs))
# [["a"]]
