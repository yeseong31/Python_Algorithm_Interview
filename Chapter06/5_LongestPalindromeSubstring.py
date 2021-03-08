# 가장 긴 팰린드롬 부분 문자열

def longestPalindrome(s: str) -> str:
    # 해당 사항 없으면 바로 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ""
    n = len(s)
    count = 0
    for start in range(n):
        end = start + count
        while end < n:
            end += 1
            w = s[start:end]
            if w == w[::-1] and len(result) < len(w):
                result = w
                count = len(result)
    return result

s = "babad"
print(longestPalindrome(s))

s = "ac"
print(longestPalindrome(s))

# 실행 시간 6792 ms
