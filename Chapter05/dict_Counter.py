# Counter 객체는 아이템에 대한 개수를 계산하여 딕셔너리로 반환한다.

from collections import Counter

a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = Counter(a)
print(b)    # Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})


# Counter 객체는 딕셔너리를 한 번 더 Wrapping한 collections.Counter 클래스를 가진다.
print(type(b))  # <class 'collections.Counter'>


# Counter 객체에서 가장 빈도 수가 높은 요소는 most_common(x)을 사용한다.
# 이때 x는 가장 빈도 수가 높은 요소를 x개 추출한다는 의미.
print(b.most_common(2))     # [(5, 3), (6, 2)]
