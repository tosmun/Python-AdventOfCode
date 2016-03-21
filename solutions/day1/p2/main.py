
floor = 0
index = 0
basement_at = None
with open('../input.txt', 'r') as fp:
	while True:
		if basement_at:
			break
		buffer = fp.read(1024)
		if buffer is None or len(buffer) <= 0:
			break
		for c in buffer:
			index += 1
			if c == '(':
				floor += 1
			elif c == ')':
				floor -= 1
			if floor < 0:
				basement_at = index
				break
print('basement at: %d' % basement_at)
