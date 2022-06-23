n=int(input()) 
for i in range(n):
    k=0 
    #l=[] 
    n1=int(input()) 
    t1=list(map(int,input().split())) 
    t1.sort(reverse=True) 
    t2=list(map(int,input().split())) 
    t2.sort(reverse=True) 
    c=0 
    for i in range(n1):
        for j in range(c,n1):
            if t1[i]>t2[j] :
                c=j+1
                k+=1 
                break 
    print(k)