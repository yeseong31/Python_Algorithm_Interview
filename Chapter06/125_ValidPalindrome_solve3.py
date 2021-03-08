# 슬라이싱 사용

# 문자열을 조작할 때는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리함.

import re

def isPalindrome(s: str):
    # 소문자화
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]     # [::-1]을 이용하면 문자열을 뒤집을 수 있음

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
