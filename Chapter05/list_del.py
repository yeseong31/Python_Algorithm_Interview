# 리스트에서 요소를 삭제하는 방법은 다음과 같이 크게 2가지가 있다.
#     인덱스로 삭제하기
#     값으로 삭제하기

a = [1, 2, 3, 5, 4, '안녕', True]

# del 키워드
del a[1]
print(a)  # [1, 3, 5, 4, '안녕', True]

# remove() 함수
a.remove(3)
print(a)  # [1, 5, 4, '안녕', True]

# pop() 함수
a.pop(3)
print(a)  # [1, 5, 4, True]
