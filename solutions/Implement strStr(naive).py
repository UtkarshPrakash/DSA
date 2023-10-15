class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        sn = len(needle)
        if sn==0:
            return 0
        for i in range(n):  # This exact sanme logic doesn't work in cpp ("mississipi" <- "issip")
            if haystack[i]==needle[0]: # Or maybe I didn't write the code properly
                for j in range(sn):
                    if i>=n:
                        return -1
                    if haystack[i]!=needle[j]:
                        break
                    i+=1
                    if j==sn-1:
                        return i-j-1
        return -1