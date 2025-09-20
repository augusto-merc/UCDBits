#include <bits/stdc++.h>

using namespace std;

int main(){

    int n, k1, k2, k3;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> k1 >> k2 >> k3;
        cout << (k1 ^ k2 ^ k3) << endl;
    }

    return 0;
}
