def main():
	#number of test cases
	N = raw_input()
	N = int(N)

	for j in range(N):
		arr = []
		input = raw_input()
		input = int(input)
		static_input = input

		i = 1

		while(True):
			if input == 0:
				print 'Case #'+ str(j+1) +': INSOMNIA'
				break 
			input = static_input * i
			str_input = list(str(input))
			for c in str_input:
				if int(c) not in arr:
					arr.append(int(c))

			if all(x in arr for x in range(10)):
				print 'Case #'+ str(j+1) +': ' + str(input)
				break
				
			i = i + 1

main()