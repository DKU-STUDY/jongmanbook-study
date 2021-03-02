#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> x(100);
vector<int> y(100);
vector<int> r(100);

struct TreeNode{
	vector<TreeNode*> chlid;
};

//제곱 연산
int sqrt(int num) {
	return num * num;
}

//a가 b를 포함하는지 판단 연산
bool enclose(int parent, int child) {
	//성벽들은 겹치거나 닿지않는다.
	//d^2 = sqrt(x[parent] - x[child]) + sqrt(y[parent] - y[child]) parent와 child원 사이의 거리
	//d == parent-child인 경우, 내부에서 접하는것임.
	//d < parent-child인 경우 , child가 내부에 있는 것임. 
	return r[parent] > r[child] && 
			sqrt(x[parent] - x[child]) + sqrt(y[parent] - y[child]) < sqrt(r[parent] - r[child]);
}

//a가 b의 자식인지 판단. 자손 아님.
bool isChild(int parent, int child) {
	//자손이 아닌경우
	if (!enclose(parent, child))
		return false;

	//자식인지 자손인지 판단.
	for (int i = 1; i < N; i++) {
		//자손인 경우
		if(i!=parent&&i!=child&&enclose(parent,i)&&enclose(i,child))
			return false;
	}
	return true;
}

//트리생성
//재귀적으로 생성한다.
TreeNode* getTree(int root) {
	TreeNode* newTree = new TreeNode();
	//자식을 넣는다.
	for (int i = 1; i < N; i++)
		if (isChild(root, i))
			newTree->chlid.push_back(getTree(i));
	return newTree;
}

//잎 - 루트를 계산 / 잎 - 잎를 계산
int max_height;
int height(TreeNode* root) {
	//루트가 잎 노드일경우. 자식노드가 없다 -> 깊이가 없다.
	int child_size = root->chlid.size();
	if (!child_size)
		return 0;
	//자식의 높이를 계산
	vector <int> child_height;
	for (int i = 0; i < child_size; i++)
		child_height.push_back(height(root->chlid[i]));

	//루트를 거쳐가는 잎-잎 노드의 거리를 계산
	sort(child_height.begin(), child_height.end());
	if (child_size > 1)
		max_height = max(max_height, 2 + child_height[child_size - 1] + child_height[child_size - 2]);
	
	return child_height.back() + 1;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> x[i] >> y[i] >> r[i];
		TreeNode* tree = getTree(0);
		max_height = 0;
		cout << max(max_height, height(tree)) << "\n";
	}
}