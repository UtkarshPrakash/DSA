class Solution {
public:
    int minimumSum(int num) {
        vector<int> dig;
        while(num>0){
            dig.push_back(num%10);
            num/=10;
        }
        sort(dig.begin(), dig.end());
        return (dig[0]*10+dig[3])+(dig[1]*10+dig[2]);
    }
};