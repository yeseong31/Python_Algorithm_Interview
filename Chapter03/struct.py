# 구조체

# 파이썬 3.7부터 dataclass를 지원하며,
# @dataclass 데코레이션(자바의 '어노테이션)으로 타입 힌트와 함께 활용함으로써
# 다음과 같이 class를 이용하여 구조체 형태로 정의할 수 있다.

from dataclasses import dataclass

@dataclass
class Product:
    weight: int = None
    price: float = None

apple = Product()
apple.price = 10
