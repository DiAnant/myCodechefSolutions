#include<bits/stdc++.h>
using namespace std;
#define ll long long int

int main()
{
    ll t; cin>>t;
    while(t--)
    {
        ll n; cin>>n;
        ll a[n];
        for(ll i = 0; i<n; i++)
        {
            cin>>a[i];
        }
        ll start, flag, count;
        start = 1; flag = 1; count = 0;
        for(ll i = 0; i<n; i++)
        {
            ll due = a[i];
            if(start == 1){
                if(due == 1) start = 0;
            }
            else{
                if(due == 1){
                    if(count<5){
                        flag = 0; break;
                    }
                    else count = 0;
                }
                else count ++;
            }
        }
        if(flag == 1) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}