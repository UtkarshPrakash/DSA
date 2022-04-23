class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int arr[256]={0};
        int ans=0;
        for (int i=0; i<jewels.size(); i++){
            arr[int(jewels[i])]=1;
        }
        for (int i=0; i<stones.size(); i++){
            if (arr[int(stones[i])]==1)
                ans++;
        }
        return ans;
    }
};