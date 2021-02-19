# 딕셔너리에 있는 키/값은 for 반복문으로도 조회가 가능하다.
a = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
for k, v in a.items():
    print(k, v)

# 딕셔너리의 키는 del로 삭제한다.
del a['key1']
print(a)    # {'key2':'value2', 'key3':'value3'}
