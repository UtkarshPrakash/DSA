class Solution {
public:
    string toLowerCase(string s) {
        // Method 1
        for (int i=0; i<s.length(); i++)
            s[i] = tolower(s[i]);
        return s;


        // Method 2 
        // for (int i=0; i<s.length(); i++){
        //     if (s[i]>64 && s[i]<91)
        //         s[i] += 32;
        // }
        // return s;


        // Method 3
        // use std::transform 
    }
};