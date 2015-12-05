from sets import Set
santa_cloc = (0,0)
robo_cloc = (0,0)
visited = Set([])
index = 0
with open('../input.txt', 'r') as fp:
	while True:
		buffer = fp.read(1024)
		if buffer is None or buffer == '':
			break
		for c in buffer:
			rcloc = santa_cloc if index % 2 == 0 else robo_cloc
			#West
			if c == '<':
				rcloc = (rcloc[0]-1, rcloc[1])
			#East
			elif c == '>':
				rcloc = (rcloc[0]+1, rcloc[1])
			#North
			elif c == '^':
				rcloc = (rcloc[0], rcloc[1]+1)
			#South
			elif c == 'v':
				rcloc = (rcloc[0], rcloc[1]-1)
			if index % 2 == 0:
				santa_cloc = rcloc
			else:
				robo_cloc = rcloc
			visited.add(rcloc)
			index += 1
print(len(visited))
