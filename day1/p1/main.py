
floor = 0
with open('../input.txt', 'r') as fp:
	while True:
		buffer = fp.read(1024)
		if buffer is None or len(buffer) <= 0:
			break
		for c in buffer:
			if c == '(':
				floor += 1
			elif c == ')':
				floor -= 1
print floor

