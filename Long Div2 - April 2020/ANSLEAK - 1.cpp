#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

	ll t; cin>>t;
	while(t-- )
	{
	    ll n,m,k; cin>>n>>m>>k;
	    vector <ll> ans;
	    for(ll i = 0; i < n; i++)
	    {
	        ll this_one = -1;
	        unordered_map <ll, ll> map;
	        for(ll j = 0; j < k; j++)
	        {
	            ll lol; cin>>lol;
	            map[lol] ++;
	            if(map[lol] > this_one){
	                this_one = map[lol];
	            }
	        }
	        for(auto x: map){
	            if(x.second == this_one){
	                ans.push_back(x.first);
	                break;
	            }
	        }
	    }
	    for(ll i = 0; i <n; i++){
	        cout<<ans[i]<<' ';
	    }
	    cout<<endl;
	}
	return 0;
}
