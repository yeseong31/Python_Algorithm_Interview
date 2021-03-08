# 여러 가지 정렬 방법

# sorted() 함수는 리스트 뿐만 아니라, 숫자, 문자로 정렬 가능하다.
a = [2, 5, 1, 9, 7]
print(sorted(a))
b = 'zbdaf'
print(sorted(b))

# sorted() 함수는 리스트를 반환하는데, 이를 문자열로 결합하려면 join() 함수를 사용한다.
print(''.join(sorted(b)))

# sort() 함수는 리스트 자체를 제자리 정렬한다. (리턴값 없음)
a.sort()

# sorted()는 또한 key= 옵션을 지정하여 정렬을 위한 키 또는 함수를 별도로 지정할 수 있다.
c = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(c, key=len))

d = ['cde', 'cfc', 'abc']
def fn(s):
    return s[0], s[-1]  # 첫 문자열과 마지막 문자열 순으로 정렬
print(sorted(d, key=fn))

# 다음과 같이 람다를 이용하면 함수를 별도로 정의하지 않고 한 줄로 처리할 수 있다.
print(sorted(d, key=lambda x: (x[0], x[1])))
