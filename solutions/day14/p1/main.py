
sec = 2503
if __name__ == '__main__':
	map = { }
	state = { }
	with open('../input.txt', 'r') as fp:
		while True:
			line = fp.readline()
			if line is None or line == '':
				break
			parts = line.split(' ')
			rd = parts[0]
			speed = int(parts[3])
			fly_time = int(parts[6])
			rest_time = int(parts[13])
			map[rd] = (speed, fly_time, rest_time)
			state[rd] = (0, 0)
	#For each second
	while sec > 0:
		sec -= 1
		for rd in map:
			rd_state = state[rd][0]
			rd_dist = state[rd][1]
			#Switch to resting
			if rd_state >= map[rd][1]:
				rd_state = -1 * map[rd][2]
			rd_state += 1
			if rd_state > 0:
				rd_dist = rd_dist + map[rd][0]
			state[rd] = (rd_state, rd_dist)
	#Find winner
	winner = (-1, None)
	for rd in state:
		if state[rd][1] > winner[0]:
			winner = (state[rd][1], rd)
	print("%s: %d" % (winner[1], winner[0]))
