t = int(input())
for x in range(1, t+1):
    m = input()
    arr = m.split()
    a = int(arr[0])
    b = int(arr[1])
    c = int(arr[2])
    n = int(arr[3])
    if (a>=b and a>=c):
        maxi = a
    if (b>=a and b>=c):
        maxi = b
    if (c>=a and c>=b):
        maxi = c
    if (a<=b and a<=c):
        mini = a
    if (b<=a and b<=c):
        mini = b
    if (c<=a and c<=b):
        mini = c
    
    if ((a>=b and a<=c) or (a<=b and a>=c)):
        mid = a
    if ((b<=a and b>=c) or (b>=a and b<=c)):
        mid = b
    if ((c<=a and c>=b) or (c>=a and c<=b)):
        mid = c
    
    A = int(maxi - mini)
    B = int(maxi - mid)

    #(n+mini >= maxi) and (n+mid >= maxi) 
    
    if ((mid + (n - (maxi - mini))) >= maxi):
        
        if (((n - (A+B))%3 == 0) and ((int(mini) + A) == (int(mid) + B))) :
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
