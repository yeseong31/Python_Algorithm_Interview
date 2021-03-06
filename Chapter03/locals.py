# locals()

# 로컬 심볼 '테이블 딕셔너리'를 가져오는 메소드
# 로컬 스코프에 제한하여 정보를 조회할 수 있기 때문에
# 클래스의 특정 메소드 내부에서나 함수 내부의 로컬 정보를 조회하여
# 잘못 선언한 부분이 없는지 확인하는 용도로 활용할 수 있다.

# 변수명을 일일이 찾아낼 필요 엾이 로컬 스코프에 정의된 모든 변수를 출력 가능.

import pprint
pprint.pprint(locals())

# 클래스 메소드 내부의 모든 로컬 변수를 출력해 주므로 디버깅에 용이.
