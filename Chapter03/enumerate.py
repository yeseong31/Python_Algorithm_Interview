# enumerate

# 순서 있는 자료형(list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴.
a = [1, 2, 3, 2, 45, 2, 5]
print(list(enumerate(a)))   # 인덱스 자동 부여


# 다음의 두 문장은 동일한 결과를 출력하는 코드
for i in range(len(a)):
    print(i, a[i], end=' / ')   # 값 조회의 과정이 한 번 더 필요(a[i])
print()

for i, v in enumerate(a):
    print(i, v, end=' / ')  # enumerate()를 활용하는 쪽이 더 간결하다.
