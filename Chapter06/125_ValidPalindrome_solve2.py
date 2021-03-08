# 데크 자료형을 이용한 최적화

# 데크(Deque)를 명시적으로 선언하면 좀 더 속도를 높일 수 있다.
# 리스트의 pop(0)은 O(n)이지만 데크의 popleft()는 O(1)이다.

import collections

def isPalindrome(s: str):
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
