# s[:]
# 파이썬은 a = b와 같은 형태로 할당하면 변수의 값이 할당되는 것이 아니라
# a 변수가 b 변수를 참조하는 형태가 된다.
# 참조가 아닌 값을 복사하기 위해 [:]를 사용할 수 있으며,
# 이 방식은 문자열이나 리스트를 복사하는 파이썬다운 방식(Pythonic Way)이기도 하다.

a = "안녕하세요"
b = a[:]

print(b[:])