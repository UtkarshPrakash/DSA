class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        arr=[0]*256
        for i in jewels:
            arr[ord(i)]=1
        for i in stones:
            if arr[ord(i)]:
                ans+=1
        return ans