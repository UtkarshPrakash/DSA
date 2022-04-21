class Solution:
    def minimumSum(self, num: int) -> int:
        dig = []
        while(num>0):
            dig.append(num%10)
            num//=10
        dig.sort()
        return (dig[0]*10+dig[3])+(dig[1]*10+dig[2])