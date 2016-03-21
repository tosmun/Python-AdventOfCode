
#0 == off
#1 == on

grid_x = 1000
grid_y = 1000
grid = { }
#initialize grid
for x in range(0,grid_x):
	for y in range(0,grid_y):
		grid[(x,y)] = 0

with open('../input.txt', 'r') as fp:
	while True:
		line = fp.readline()
		if line is None or line == '':
			break
		line = line.strip()
		if line == '':
			break
		parts = line.split(' ')
		second = [int(i) for i in parts[-1].split(',')]
		first = [int(i) for i in parts[-3].split(',')]
		action = parts[-4]
		for x in range(first[0], second[0]+1):
			for y in range(first[1], second[1]+1):
				if action == 'on':
					val = 1
				elif action == 'off':
					val = 0
				elif action == 'toggle':
					val = 1 - grid[(x,y)]
				grid[(x,y)] = val
on_count = 0
#Find lights that are on
for value in grid.values():
	if value == 1:
		on_count += 1
print("lights on: %d" % on_count)
