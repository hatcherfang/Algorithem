#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> nums;
    int temp;
    while (cin >> temp)
        nums.push_back(temp);

    int ans = 0;
    for (auto x: nums)
        ans ^= x;

    cout << ans << endl;
    
    return 0;
}
