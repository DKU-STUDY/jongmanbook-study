//���� ���� �˰��� ����
/*
ù° �ٿ��� ��ü ������ �� ���� ���� N�� �־��� �ִ�. N�� 2, 4, 8, 16, 32, 64, 128 �� �ϳ��̴�. 
�������� �� �������� ���簢��ĭ���� ���� ���ٺ��� ���ʷ� ��° �ٺ��� ������ �ٱ��� �־�����. 
�Ͼ������ ĥ���� ĭ�� 0, �Ķ������� ĥ���� ĭ�� 1�� �־�����, �� ���� ���̿��� ��ĭ�� �ϳ��� �ִ�.
*/

#include <iostream>

using namespace std;

int paper[128][128];
int white_cnt = 0;
int blue_cnt = 0;

void divide_and_conquer(int from_y, int from_x, int d) {
	bool flag = false;
	int check_arr = paper[from_y][from_x];
	for (int y = from_y; y < from_y + d && !flag; y++) {
		for (int x = from_x; x < from_x + d; x++) {
			if (check_arr != paper[y][x]) {
				flag = !flag;
				break;
			}
		}
	}
	if (flag) {
		divide_and_conquer(from_y, from_x, d / 2);
		divide_and_conquer(from_y, from_x + d / 2, d / 2);
		divide_and_conquer(from_y + d / 2, from_x, d / 2);
		divide_and_conquer(from_y + d / 2, from_x + d / 2, d / 2);
	}
	else {
		if (check_arr)
			blue_cnt++;
		else
			white_cnt++;
	}
	return;
}

int main() {
	int N;
	cin >> N;
	for (int y = 0; y < N; y++)
		for (int x = 0; x < N; x++)
			cin >> paper[y][x];
	divide_and_conquer(0, 0, N);
	cout << white_cnt << "\n" << blue_cnt;
}