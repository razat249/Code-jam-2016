

def further_states(s, level):
	i = 0
	while i < len(s):
		temp_s = s[:i+1]
		temp_s = temp_s[::-1]
		temp_s = list(temp_s)
		j = 0
		while j < len(temp_s):
			if temp_s[j] == '+':
				temp_s[j] = '-'
			else:
				temp_s[j] = '+'
			j = j + 1
		temp_s = ''.join(temp_s)
		to_append = (temp_s + s[len(temp_s):],level+1)
		if to_append not in traversed and to_append not in to_traverse:
			to_traverse.append(to_append)
		i = i + 1

def bfs(input):
	final_str = '+' * len(input)
	while (True):
		to_check = to_traverse.pop(0)
		traversed.append(to_check)
		if to_check[0] != final_str:
			further_states(to_check[0], to_check[1])
		else:
			yield to_check[1]

def main():
	T = raw_input()
	T = int(T)
	i = 0
	while i < T:
		i = i + 1
		global traversed
		global to_traverse
		traversed = []
		to_traverse = []
		input = raw_input()
		to_traverse.append((input, 0))
		print 'Case #'+str(i)+': '+ str(bfs(input).next())

main()
