#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

//arr의 최대 사각형을 반환합니다.
int max_square(vector<int> arr) {
	//스택에는 left는 정해졌지만 right가 정해지지 않은 판자의 번호가 있습니다.
	stack <int> st;
	//인덱스 -1은 0의 판자길이를 가집니다.
	int size = arr.size();
	int res = 0;
	//오른쪽을 탐색합니다. 오른쪽을 발견한경우 left / right 범위를 계산해서 최대 사각형을 구합니다.
	//해당 오른쪽이 자신의 오른쪽이 아닐수있습니다.
	//왼쪽, 오른쪽은 경계로써 자신보다 작은 판자가 들어갑니다.
	for (int i = 0; i + 1 < size; i++) {;
		//아직 오른쪽 검사를 하지 않았다 -> 모른다 -> 넣는다. -> 검사에 맡긴다.
		st.push(i);
		int right = i + 1;
		//스택의 오른쪽이 정해진경우
		while (!st.empty()&&arr[st.top()] >= arr[right]) {
		//정해졌으니 pop한다.
			int current_idx = st.top();
			st.pop();
		//왼쪽은 이미 정해져있다.
			int left = st.empty() ? -1 : st.top();
			int width = right - left - 1;
			res = max(res, width * arr[current_idx]);
		}
	}
	return res;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		vector<int> arr(N);
		int number;
		for (int i = 0; i < N; i++)
			cin >> arr[i];
		arr.push_back(0);
		cout << max_square(arr) << "\n";
	}
}
