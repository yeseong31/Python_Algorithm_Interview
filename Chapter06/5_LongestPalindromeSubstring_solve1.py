# 가장 긴 팰린드롬 부분 문자열 - 중앙을 중심으로 확장하는 풀이

# 이 문제는 '다이나믹 프로그래밍'으로 풀 수 있지만,
# 이는 직관적으로 이해가 어렵고, 일반적인 예상과는 달리 실행 속도도 느리므로
# '투 포인터'가 중앙을 중심으로 확장하는 형태를 이용하여 해결하도록 한다.

# 2칸(짝수), 3칸(홀수)으로 구성된 투 포인터가 '슬라이딩 윈도우(ch20)'처럼 계속 앞으로 전진한다.
# 이때 윈도우에 들어온 문자열이 팰린드롬이라면, 그 자리에 멈추고, 투 포인터를 확장한다.
# 팰린드롬은 bb처럼 짝수이거나, bab처럼 홀수일 때도 있으므로 짝수, 홀수 모든 경우에 대해 판별한다.


def longestPalindrome(s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        # 중앙을 기준으로 좌우가 같으면 계속 팰린드롬임.
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]
    
    # 해당 사항이 없으면 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ""
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),  # 짝수
                     expand(i, i + 2),  # 홀수
                     key=len)
    return result

s = "babad"
print(longestPalindrome(s))

s = "ac"
print(longestPalindrome(s))

# 실행 시간 284 ms
