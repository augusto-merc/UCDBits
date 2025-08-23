#include<bits/stdc++.h>
using namespace std;

int main(){

    int d, l, c, h;

    cin >> d;
    cin >> l >> c >> h;

    cout << ((d <= l && d <= c && d <= h) ? 'S' : 'N') << endl;

    return 0;
}
