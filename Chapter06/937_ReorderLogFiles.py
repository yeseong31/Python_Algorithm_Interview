# 로그 파일 재정렬

# 1. 로그의 가장 앞 부분은 식별자
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순으로 한다.

def reorderLogFiles(logs):
    alpha, num = [], []
    # 문자인지 숫자인지 판별
    for log in logs:
        if log.split()[1].isdigit():
            num.append(log)
        else:
            alpha.append(log)
    # 문자의 경우만 정렬하면 됨
    alpha = sorted(alpha, key=lambda x: (x.split()[1:], x.split()[0]))
    return alpha + num
    

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))
# 출력1
# ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(reorderLogFiles(logs))
# 출력2
# ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
