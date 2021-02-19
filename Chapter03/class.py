# 클래스

# dataclass 데코레이션을 이용하여 클래스를 선언할 수도 있다.
# 이를 선언하지 않아도 문제는 없으나, 선언하게 되면 여러 가지
# 내부 함수의 기능도 자동으로 구현해주므로 편리하게 활용할 수 있다.

from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area())
