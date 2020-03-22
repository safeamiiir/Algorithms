#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll answer = 0;
vector<pair<int, int>> mergesort(vector<pair<int, int>>& arr) {
	int n = arr.size();
	if(n == 1) {
		return arr;
	}
	
	int mid = n/2;
	vector<pair<int, int>> left, right;
	for(int i = 0; i < mid; i++) {
		left.push_back(arr[i]);
	}
	
	for(int i = mid; i < n; i++) {
		right.push_back(arr[i]);
	}
	
	left = mergesort(left);
	right = mergesort(right);
	
	vector<ll> pre = {right.back().first};
	int sz = right.size();
	for(int i = sz-2; i >= 0; i--) {
		pre.push_back(pre.back() + right[i].first);
	}
	
	arr.clear();
	int i = 0, j = 0;
	while(i < (int) left.size() && j < (int) right.size()) {
		int v_i = left[i].second;
		int v_j = right[j].second;
		if(v_i <= v_j) {
			int m = pre.size();
			ll all = pre.back();
			answer += all - ll(m)*ll(left[i].first);
			arr.push_back(left[i++]);
		} else {
			arr.push_back(right[j++]);
			pre.pop_back();
		}
	}
	while(i < (int) left.size()) {
		arr.push_back(left[i++]);
	}
	while(j < (int) right.size()) {
		arr.push_back(right[j++]);
	}
	return arr;
}
int main() {
	cin.tie(0);
	int n;
	cin >> n;
	vector<pair<int, int>> arr(n);
	for(int i = 0; i < n; i++) {
		cin >> arr[i].first;
	}
	for(int i = 0; i < n; i++) {
		cin >> arr[i].second;
	}
	sort(arr.begin(), arr.end());
	arr = mergesort(arr);
	cout << answer << endl;
	return 0;
}
