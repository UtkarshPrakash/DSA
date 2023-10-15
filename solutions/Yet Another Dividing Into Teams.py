team = 1

q = int(input())

for x in range(q):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	team = 1
	diff = [a[i+1] - a[i] for i in range(len(a) - 1)]
	for j in diff:
	    if ((j == 1) and len(a) > 1) :
	        team = 2
	        break
	    else :
	    	team = 1
	print(team)    	
	        