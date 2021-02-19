# 제네릭 프로그래밍

# def are_equal(a, b):
#   return a == b
  
# are_equal(10, 10.0)
 
# 파이썬은 원래 동적 타이핑 언어이므로 제네릭이 필요 없지만
# 타입을 아예 명시하지 않으면 가독성을 낮추고 버그 발생 확률이 높아진다.
# 따라서 다음과 같이 타입을 명시할 수 있다.
 
 from typing import TypeVar
 
 T = TypeVar('T')
 U = TypeVar('U')
 
 def are_equal(a: T, b: U) -> bool:
  return a == b
 
 are_equal(10, 10.0)
 
 # PEP 484에 추가된 타입 힌트를 통해 이처럼 제네릭을 사용할 수 있다.(단, 3.5+에서만)
