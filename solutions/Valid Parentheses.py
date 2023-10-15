class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = {'(':')', '[':']', '{':'}'}
        cl = [')', '}', ']']
        if s[0] in cl:
            return False
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i] in cl:
                if len(stack)==0:
                    return False
                if s[i]==op[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack)==0:
            return True
        else:
            return False