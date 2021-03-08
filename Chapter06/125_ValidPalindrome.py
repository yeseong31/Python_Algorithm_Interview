# 유효한 팰린드롬
# 주어진 문자열이 팰린드롬인지 확인하라.

# '팰린드롬' = 앞뒤가 똑같은 '회문'


def isPalindrome(s: str):
    tmp = []
    for c in s:
        if c.isalnum():     # isalnum(): 영문자나 숫자인지 판단
            tmp.append(c.lower())
    return tmp == tmp[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))



