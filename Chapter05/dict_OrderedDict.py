# OrderedDict 객체
# 대부분의 언어에서 해시 테이블을 이용한 자료형은 입력 순서가 유지되지 않는다.
# 이에 파이썬 3.6 이하에서는 입력 순서가 유지되는 OrderedDict라는 별도의 객체를 제공했다.

from collections import OrderedDict

print(OrderedDict({'banana':3, 'apple': 4, 'pear':1, 'orange':2}))

# 하지만 파이썬 3.7+부터 딕셔너리는 내부적으로 인덱스를 이용하며 입력 순서가 유지된다.
# 그러나 원래 해시 테이블은 입력 순서에 관여하지 않는 자료형이므로,
# 무턱대고 딕셔너리로 입력 순서를 기대하는 것은 매우 위험하다.
