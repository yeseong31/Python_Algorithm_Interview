# range

# 제너레이터의 방식을 활용하는 대표적인 함수

import sys

# 다음은 숫자 100만 개를 생성하는 2가지 방법이다.
a = [n for n in range(1000000)] 
b = range(1000000)

# 둘 다 동일한 100만 개의 숫자를 저장하지만
# range 클래스를 이용하는 변수 b의 메모리 점유율이 압도적으로 작다.
# '생성 조건(range 클래스)'만을 보관하고 있기 때문이다.
print(sys.getsizeof(a))    # 8448728
print(sys.getsizeof(b))    # 48
print(b[999])   # 리스트와 사용 방법은 거의 동일
