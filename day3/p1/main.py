from sets import Set
cloc = (0, 0)
visited = Set([])
with open('../input.txt', 'r') as fp:
	while True:
		buffer = fp.read(1024)
		if buffer is None or buffer == '':
			break
		for c in buffer:
			#West
			if c == '<':
				cloc = (cloc[0]-1, cloc[1])
			#East
			elif c == '>':
				cloc = (cloc[0]+1, cloc[1])
			#North
			elif c == '^':
				cloc = (cloc[0], cloc[1]+1)
			#South
			elif c == 'v':
				cloc = (cloc[0], cloc[1]-1)
			visited .add(cloc)
print(len(visited))
