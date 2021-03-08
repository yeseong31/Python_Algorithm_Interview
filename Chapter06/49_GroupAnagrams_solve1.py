# 그룹 애너그램 - 정렬하여 딕셔너리에 추가

# 애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것.
# 애너그램 관계인 단어들을 정렬하면, 서로 같은 값을 갖게 되기 때문이다.

# sorted()의 리턴값을 키로 사용하기 위해 join()으로 합치는 것이 포인트.
# 존재하지 않는 키를 딕셔너리에 삽입하게 되면 에러가 발생하므로 defaultdict() 사용

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()
