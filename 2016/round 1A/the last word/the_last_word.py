T = int(raw_input())
for n in range(T):	
	S = raw_input()
	result = ''
	current = S[0]

	for i in S:
		if i >= current:
			result = i + result
			current = i
		else:
			result = result + i

	print 'Case #'+ str(n+1) +': ' + result