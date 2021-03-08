# 가장 흔한 단어 - 리스트 컴프리헨션, Counter 객체 사용

# 입력값에서는 대소문자가 섞여 있으며 구두점이 존재하므로
# '데이터 클렌징'이라 부르는 입력값에 대한 전처리 작업이 필요하다.

import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # 문자열 앞에 r이 붙으면 해당 문자열이 구성된 그대로 문자열로 반환
        words = [w for w in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                     if w not in banned]
        return collections.Counter(words).most_common(1)[0][0]

#       defaultdict()를 사용하여 int 기본값이 자동으로 부여
#       counts에서 값이 가장 큰 키를 가져온다. (= 수학에서의 argmax)
#       하지만 Counter 모듈을 사용하면 좀 더 깔끔하게 처리할 수 있다.

#       counts = collections.defaultdict(int)
#       for word in words:
#           counts[word] += 1
#       print(max(counts, key=counts.get))

