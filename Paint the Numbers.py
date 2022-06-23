n = int(input())
m = list(map(int,input().split()))
m.sort()
print(m)
for x in range(n-1):
	for y in range(n-1):
		if (m[y]%m[x]==0 and x!=y):
			m.remove(m[y])

print(m)			