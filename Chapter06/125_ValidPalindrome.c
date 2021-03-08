#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

// 문자열을 저장하는 char 포인터에 대한 직접 조작으로 가능한 한 빠르게 동작하도록 함.
// 위치 포인터를 직접 조작하기 때문에 매우 빠르게 실행된다.

bool isPalindrome(char* s) {
	int bias_left = 0;
	int bias_right = 1;
	
	int str_len = strlen(s);
	for (int i = 0; i < str_len; i++) {
		// 스킵 포인터 처리
		while (!isalnum(s[i + bias_left])) {
			bias_left++;
			if (i + bias_left == str_len)
				return true;
		}
		while (!isalnum(s[str_len - i - bias_right]))
			bias_right++;

		if (i + bias_left >= str_len - i - bias_right)
			break;
		// 팰린드롬 비교
		if (tolower(s[i + bias_left]) != tolower(s[str_len - i - bias_right]))
			return false;
	}
	return true;
}

int main(void) {
	char s[] = "A man, a plan, a canal: Panama";
	if (isPalindrome(s))
		printf("true\n");
	else
		printf("false\n");
}