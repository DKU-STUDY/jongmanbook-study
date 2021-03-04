//비가 내리면 달팽이는 하루에 2미터를 기어올라갈수있다.
//날이 맑으면 1미터밖에 올라가지 못한다.
//m일간 각 날짜에 비가 올 확률이 정확히 75%이다.
//m일 안에 달팽이가 우물 끝까지 올라갈 확률은?
//climb(days, climbed) --> days동안 climbed만큼 올라갔을때, m일안에 n이상 올라갈 확률. 메모이제이션을 위해서 과거의 인자를 최대한 줄인다.
//climb(days, climbed) = 0.75 * climb(days+1, climbed+2) + 0.25 * climb(days+1, climbed+1)
//즉 다음날에 비가올확률에 75% . 오지 않을 확률에 25%를 곱한것의 합이 전채 확률이다. --> 상당히 직관적이다.
#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;

vector<int> order(int city_nodes, vector<int> city_from, vector<int> city_to, int company) {
    vector <vector<int>> node(city_nodes + 1);
    bool check[10001];
    for (int i = 1; i <= city_nodes; i++)
        check[i] = false;

    for (int i = 0; i < city_nodes; i++) {
        node[city_from[i]].push_back(city_to[i]);
        node[city_to[i]].push_back(city_from[i]);
    }

    vector<int> res;
    queue <int> q;
    q.push(company);
    check[company] = true;
    while (!q.empty()) {
        int spot = q.front();
        q.pop();
        check[spot] = true;
        sort(node[spot].begin(), node[spot].end());
        for (int w : node[spot]) {
            if (!check[w]) {
                res.push_back(w);
                q.push(w);
                check[w] = true;
            }
        }

    }
    return res;
}

int main() {
    order(5,{1,1,2,3,1}, {2,3,4,5,5}, 1);
}