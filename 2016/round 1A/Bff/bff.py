N = 4
l = [7, 8, 10, 10, 9, 2, 9, 6, 3, 3]
result = []

index = 1
for i in l:
	if l[index-1] and l[index-1] not in result:
		result.append(l[index-1])
		index = l[index-1]
	else:
		if l.index(l[-1]) not in result:
			result.append(l.index(l[-1]))	

print result