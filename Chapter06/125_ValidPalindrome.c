#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

// ���ڿ��� �����ϴ� char �����Ϳ� ���� ���� �������� ������ �� ������ �����ϵ��� ��.
// ��ġ �����͸� ���� �����ϱ� ������ �ſ� ������ ����ȴ�.

bool isPalindrome(char* s) {
	int bias_left = 0;
	int bias_right = 1;
	
	int str_len = strlen(s);
	for (int i = 0; i < str_len; i++) {
		// ��ŵ ������ ó��
		while (!isalnum(s[i + bias_left])) {
			bias_left++;
			if (i + bias_left == str_len)
				return true;
		}
		while (!isalnum(s[str_len - i - bias_right]))
			bias_right++;

		if (i + bias_left >= str_len - i - bias_right)
			break;
		// �Ӹ���� ��
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