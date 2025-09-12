#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, n, k;

    cin >> t;
    vector<int> results;
    results.reserve(t);
    while (t--) {
        cin >> n >> k;

        if (n >> 1){
            results.push_back(1 + ceil((double)((n - k) / (k - 1))));
        } else {
            results.push_back(ceil((double)(n / k)));
        }
    }

    for (const auto &result : results) {
        cout << result << "\n";
    }
    return 0;
}
