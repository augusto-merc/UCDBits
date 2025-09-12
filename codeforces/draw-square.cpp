#include <bits/stdc++.h>

using namespace std;

int main(){

    int t, l, r, d, u;
    vector<string> results;

    cin >> t;

    while(t--){

        cin >> l >> d >> r >> u;

        if (l == r && r == d && d == u){
            results.push_back("YES");
        }
        else {
            results.push_back("NO");
        }

    }

    for (auto result : results){
        cout << result << endl;
    }

}