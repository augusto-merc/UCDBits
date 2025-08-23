#include <bits/stdc++.h>
using namespace std;

int main(){
    
    int n, e = 0, c = 0, s = 0;

    cin >> n;

    int x[n];

    for (int i = 0; i < n; i++){
        cin >> x[i];
        s += x[i];
    }

    int i = 0;
    while (i < 0 || i > n-1){
        if (x[i] == 0){
            break;
        }

        if (x[i] % 2 != 0){
            e++;
            c++;
            x[i]--;
            i++;
        } else{
            e++;
            c++;
            x[i]--;
            i--;
        }
    }

    cout << e << " " << s - c << endl; 

    return 0;
}
