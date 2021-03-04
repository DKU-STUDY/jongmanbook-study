#include <iostream>
#include <vector>

using namespace std;

void post_order(const vector<int>& pre_order, const vector<int>& in_order) {
	if (!pre_order.size())
		return;
	int root_node = pre_order[0];
	//root_node의 왼쪽 노드 끝범위(미포함)
	int L = find(in_order.begin(), in_order.end(), root_node) - in_order.begin();
	vector<int> pre_left(pre_order.begin() + 1, pre_order.begin() + L + 1);
	vector<int> pre_right(pre_order.begin() + L + 1, pre_order.end());
	
	vector<int> in_left(in_order.begin(), in_order.begin() + L);
	vector<int> in_right(in_order.begin() + L + 1, in_order.end());

	post_order(pre_left, in_left);
	post_order(pre_right, in_right);

	cout << root_node << " ";
}

int main() {
	int N;
	cin >> N;
	vector<int> pre_order(N);
	for (int i = 0; i < N; i++)
		cin >> pre_order[i];
	vector<int> in_order(N);
	for (int i = 0; i < N; i++)
		cin >> in_order[i];
	post_order(pre_order, in_order);
}