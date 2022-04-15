class Solution:
    def mid(self, ls):
        m = len(ls)
        r = []
        for i in range(m-1):
            r.append(ls[i]+ls[i+1])
        return r
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        n = numRows
        for i in range(1, n+1):
            temp = [1]
            if i==1:
                ans.append(temp)
                continue
            if i==2:
                temp = [1,1]
                ans.append(temp)
                continue
            temp.extend(self.mid(ans[-1]))
            temp.append(1)
            ans.append(temp)
        return ans
        
            