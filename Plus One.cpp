class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        if (digits[n-1]==9){
            int carry = 1;
            digits[n-1] = 0;
            int i = n-2;
            int temp;
            while(carry>0 && i>=0){
                temp = digits[i]+carry;
                carry = 0;
                if (temp>9){
                    carry = 1;
                    digits[i] = temp-10;
                }
                else
                    digits[i] = temp;
                i--;
            }
            if (carry!=0){
                digits[0] = 1;
                digits.push_back(0);
            }
        }
        else
            digits[n-1]+=1;
        
        return digits;
                
    }
};