# '투 포인터'를 이용한 전통적인 방식
# 투 포인터란 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식을 말한다.

def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

s = ["H", "e", "l", "l", "o"]
Solution.reverseString(s)
print(s)
