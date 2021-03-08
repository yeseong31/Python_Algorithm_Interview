# 파이썬다운 방식
# 이 문제는 파이썬의 기본 기능을 이용하면 단 한 줄로 쉽게 풀이할 수 있다.

def reverseString(s):
    s.reverse()

# s = s[::-1]
# 이 풀이는 리트코드에서는 오류가 발생한다.
# 이 문제는 공간 복잡도를 O(1)로 제한하다 보니 변수 할당을 처리하는 데 제약이 있다.
# 이때 다음과 같은 트릭을 사용하면 잘 동작한다.
# s[:] = s[::-1]