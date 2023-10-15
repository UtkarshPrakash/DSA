class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> copy = nums;
        int len = copy.size();
        int l = 0;
        int r = len-1;
        int add;
        sort(copy.begin(), copy.end());
        int m;
        int n;
        while(l<r){
            add = copy[l]+copy[r];
            if (add==target){
                m = copy[l];
                n = copy[r];
                break;
            }
            if (add>target){
                r--;
            }
            else{
                l++;
            }
        }
        int a=-1;
        int b=-1;
        for (int i=0; i<len; i++){
            if (nums[i]==m && a==-1){
                a = i;
            }
            if (nums[i]==n && a!=i){
                b = i;
            }
            if (a!=-1 && b!=-1){
                break;
            }
        }
        vector<int> ans;
        ans.push_back(a);
        ans.push_back(b);
        return ans;
    }

};