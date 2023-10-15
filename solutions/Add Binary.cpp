class Solution { //Solution by Bans
public:
    string addBinary(string a, string b) {string ans="";int rem=0;
                                          int n1=a.length();int n2=b.length();
        int i=a.length()-1;int j=b.length()-1;int fi=0;int fj=0;
                                      
                                          
                                          
        while((i<n1 || j<n2 )||rem==1)
        { 
            
            if( ((a[i]-'0')+(b[j]-'0')+rem)==0)
              ans='0'+ans;
       else  if(((a[i]-'0')+(b[j]-'0')+rem)==1)
         { ans='1'+ans;rem=0;}
        else  if(((a[i]-'0')+(b[j]-'0')+rem)==2)
          {  ans='0'+ans;rem=1;}
         else if(((a[i]-'0')+(b[j]-'0')+rem)==3)
          {ans='1'+ans;rem=1;}
        if(i!=n1) i--;
            if(j!=n2)
            j--;
         if(i<0 && fi==0)
         {a=a+'0';i=a.length()-1;fi=1;}
         if(j<0 && fj==0)
         {b=b+'0';j=b.length()-1;fj=1;}
        }
        return ans;
        
    }
};