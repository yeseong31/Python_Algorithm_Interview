# 제너레이터

# 루프의 반복 동작을 제어할 수 있는 루틴 형태
# yield 구문으로 제너레이터를 리턴할 수 있음
# yield는 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 의미로
# 중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행.

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

# 제너레이터는 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능.
def type_of_generator():
    yield 1
    yield 'string'
    yield True

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))

g = type_of_generator()
print(next(g))
print(next(g))
print(next(g))
