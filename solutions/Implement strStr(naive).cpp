class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size();
        int sn = needle.size();
        if (sn==0)
            return 0;
        int temp;
        for (int i=0; i<n; i++){
            if (haystack[i]==needle[0]){
                temp = i;   // needed to store orig val of i 
                for (int j=0; j<sn; j++){
                    if (i>=n)
                        return -1;
                    if (haystack[i]!=needle[j]){
                        i = temp;
                        break;
                    }
                    i++;
                    if (j==sn-1)
                        return i-j-1;
                }
            }
            
        }
        return -1;
    }
};