class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[n-1]==9:
            carry = 1
            digits[n-1] = 0
            i = n-2
            while(carry>0 and i>=0):
                temp = digits[i] + carry
                carry = 0
                if temp>9:
                    carry = 1
                    digits[i] = temp - 10
                else:
                    digits[i] = temp
                i-=1
                    
            if carry!=0:
                new=[1]
                new.extend(digits)
                digits = new
            
                
        else:
            digits[n-1]+=1
        return digits