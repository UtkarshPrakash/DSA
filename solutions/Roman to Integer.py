class Solution:
    def romanToInt(self, s: str) -> int:
        dt = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        size = len(s)
        if size==1:
            return dt[s]
        ans = dt[s[size-1]]
        
        for i in range(size-2, -1, -1):
            if(dt[s[i+1]] > dt[s[i]] ):
                ans = ans - dt[s[i]]
            else:
                ans += dt[s[i]]
                
        return ans			
        