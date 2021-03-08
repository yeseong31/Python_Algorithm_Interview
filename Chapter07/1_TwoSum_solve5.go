// 고(Go)

// 파이썬과 동일한 로직으로 '고 언어'로 작성하여 얼마나 시간이 걸리는지 측정해 보자.

func twoSum(nums []int, target int) [] int {
	numsMap := make(map[int]int)

	// 키와 값을 바꿔서 딕셔너리로 저장
	for i, n := range nums {
		numsMap[n] = i
	}
	
	// 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
	for i, n := range nums {
		if j, ok := numsMap[target - n]; ok && i != j {
			return []int{i, j}
		}
	}
	
	return []int{}
}

// runtime: 4 ms
