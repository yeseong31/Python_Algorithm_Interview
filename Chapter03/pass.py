# pass

# '널 연산'으로 아무것도 하지 않는 기능
# 목업(mockup) 인터페이스부터 구현한 다음에 추후 구현을 진행할 수 있도록 함.
# 온라인 코딩 테스트 시에도 무척 유용함.

class MyClass(object):
    def method_a(self):
        pass    # 아무 기능 없음
    def method_b(self):
        print('Method B')

c = MyClass()
c.method_b()
