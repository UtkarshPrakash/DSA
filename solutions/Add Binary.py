class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = len(a)
        nb = len(b)
        ans = ''
        carry = 0
        if na==nb:
            n = na
            for i in range(n-1, -1, -1):
                temp = int(a[i])+int(b[i])+carry
                carry = 0
                if temp==0:
                    ans = '0'+ans
                elif temp==1:
                    ans = '1'+ans
                elif temp==2:
                    ans = '0'+ans
                    carry = 1
                elif temp==3:
                    ans = '1'+ans
                    carry = 1
            if carry==0:
                return ans
            else:
                return '1'+ans
        if na>nb:
            major = a
            len_big = na
            minor = b
            len_sm = nb
        else:
            major = b
            len_big = nb
            minor = a
            len_sm = na
        for i in range(len_big-len_sm):
            minor = '0'+minor
        n = len_big
        for i in range(n-1, -1, -1):
            temp = int(major[i])+int(minor[i])+carry
            carry = 0
            if temp==0:
                ans = '0'+ans
            elif temp==1:
                ans = '1'+ans
            elif temp==2:
                ans = '0'+ans
                carry = 1
            elif temp==3:
                ans = '1'+ans
                carry = 1
        if carry==0:
            return ans
        else:
            return '1'+ans
