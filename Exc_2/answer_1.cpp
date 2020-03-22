#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef
tree<
	pair<int, int>,
	null_type,
	less<pair<int, int>>,
	rb_tree_tag,
	tree_order_statistics_node_update>
ordered_set;

int main() {
	int number;
	cin >> number;
	vector<pair<int, int>> p(number);
	for (auto &pnt : p) cin >> pnt.first;
	for (auto &pnt : p) cin >> pnt.second;
	sort(p.begin(), p.end());
	ordered_set s;
	long long answer = 0;
	for(int i = 0; i < number; ++i) {
		int counter = s.order_of_key(make_pair(p[i].second + 1, -1));
		answer += counter * 1ll * p[i].first;
		s.insert(make_pair(p[i].second, i));
	}
	s.clear();
	for(int i = number - 1; i >= 0; --i) {
		int counter = int(s.size()) - s.order_of_key(make_pair(p[i].second - 1, number));
		answer -= counter * 1ll * p[i].first;
		s.insert(make_pair(p[i].second, i));
	}
	cout << answer << endl;
	return 0;
}
