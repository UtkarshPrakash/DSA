class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int n = accounts.size();
        int ans=INT_MIN; //min val possible in int cpp
        int m;
        int curr;
        for(int i=0; i<n; i++){
            m = accounts[i].size();
            curr = 0;
            for(int j=0; j<m; j++){
                curr += accounts[i][j];
            }
            
            ans = max(curr, ans);
        }
        return ans;
    }
};