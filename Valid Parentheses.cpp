class Solution {
public:
    bool isValid(string s) {
        stack<string> stack;
        string op[] = {'(', '{', '['};
        string cl[] = {')', '}', '['};
        if (find(cl, cl+3, s[0]))
            return false;
        stack.push(s[0]);
    }
};