# 로그 파일 재정렬 - 람다와 + 연산자를 이용

# 먼저, 문자로 구성된 로그가 숫자 로그보다 이전에 오며, 숫자 로그는 입력 순서대로 둔다.
# 문자 로그를 정렬한 후, 식별자를 제외한 문자열 [1:]을 키로 하여 정렬하며,
# 동일한 경우 후순위로 식별자 [0]를 지정해 정렬되도록, '람다 표현식'을 이용하여 정렬한다.

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
