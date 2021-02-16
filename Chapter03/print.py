# print

# 코딩 테스트 시에는 디버거를 사용하거나 TDD 방식으로 접근하는 것이 어려우므로
# 사실상 print()가 디버깅을 위해 제공되는 유일한 기능이기도 하다.

# 콤마(,)
print('A1', 'B2')

# sep 파라미터로 구분자 지정
print('A1', 'B2', sep=',')

# 줄바꿈 제한
print('aa', end=' ')
print('bb')

# join()으로 묶어 리스트를 출력
a = ['A', 'B']
print(' '.join(a))

# format
idx = 1
fruit = 'Apple'
print('{0}: {1}'.format(idx, fruit))

# f-string 사용으로 format의 사용보다 더 간편함(단, python 3.6+에서만 동작)
print(f'{idx}: {fruit}')
