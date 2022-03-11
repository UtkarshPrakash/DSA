class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> check;
        int n = nums.size();
        for (int i=0; i<n; i++){
            if (check[nums[i]]){
                return true;
            }
            check[nums[i]] = 1;
        }
        return false;
    }
};