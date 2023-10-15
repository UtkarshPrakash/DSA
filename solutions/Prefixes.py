length = int(input())
s = str(input())
counter = 0

string = []

string.extend(s)

for i in range(0, len(string) - 1, 2):
	if (string[i] == string[i+1]):
		if (string[i] == 'a'):
			string[i] = 'b'
			counter += 1

		elif (string[i] == 'b'):
			string[i] = 'a'
			counter += 1

		else :
			pass		
    
	
print(counter)

for j in string:
	print(j, end='')