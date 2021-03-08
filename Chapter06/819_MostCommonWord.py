# 가장 흔한 단어
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자를 구분하지는 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # 구두점 제거: [^\w] -> 단어가 아닌 경우에 한함
        words = re.sub('[^\w]', ' ', paragraph).lower().split()
        words = [w for w in words if w not in banned]
        return Counter(words).most_common(1)[0][0]
        

solution = Solution()

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(solution.mostCommonWord(paragraph, banned))
# "ball"

paragraph = "a."
banned = []
print(solution.mostCommonWord(paragraph, banned))
# "a"
