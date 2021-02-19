# defaultdict 객체는 존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하는 대신
# 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해준다.

from collections import defaultdict

a = defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a)    # defaultdict(<class 'int'>, {'A': 5, 'B': 4})

# 아래의 'C'는 존재하지 않는 키이므로 KeyError가 발생하겠지만,
# defaultdict 객체는 에러 없이 바로 +1 연산이 가능하고
# 이 경우 디폴트인 0을 기준으로 자동 생성한 후 연산 수행이 가능하도록 한다.
a['C'] += 1
print(a)    # defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})
