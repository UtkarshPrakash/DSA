class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        char op[] = {'(', '{', '['};
        char cl[] = {')', '}', ']'};
        map<char, char> open;
        open.insert(pair<char,char>('(', ')'));
        open.insert(pair<char,char>('{','}'));
        open.insert(pair<char,char>('[',']'));
        if (s[0]==')' || s[0]=='}' || s[0]==']')
            return false;
        stack.push(s[0]);
        for (int i=1; i<s.length(); i++){
            if (s[i]==')' || s[i]=='}' || s[i]==']'){
                if (!stack.size())
                    return false;
                if (s[i]==open[stack.top()])
                    stack.pop();
                else
                    return false;
            }
            else
                stack.push(s[i]);
        }
        if (stack.size())
            return false;
        else
            return true;
    }
};