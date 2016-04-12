def num(n,list_len_input,list_input,credit_input):
	for i in range(list_len_input):
		for j in range(list_len_input):
			if list_input[i] + list_input[j] == credit_input and i != j:
				return 'Case #'+ str(n + 1) +': ' + str(i+1) + ' ' + str(j+1)

def main():
	N = int(raw_input())

	for n in range(N):
		credit_input = int(raw_input())
		list_len_input = int(raw_input())
		list_input = [int(x) for x in raw_input().split(" ")]
		print num(n,list_len_input,list_input,credit_input)

main()