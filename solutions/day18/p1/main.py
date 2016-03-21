
x_len = 100
y_len = 100
steps = 100

def new_grid():
	ng = [ ]
	for x in range(x_len):
		ng.append([])
		for y in range(y_len):
			ng[x].append(0)
	return ng

def main():
	g = new_grid()
	with open('../input.txt', 'r') as fp:
		for x in range(x_len):
			for y in range(y_len):
				c = None
				while c not in ['#','.']:
					c = fp.read(1)
					if c is None or c == '':
						raise Exception("Not enough input")
				g[x][y] = (1 if c == '#' else 0)
	for i in range(steps):
		new_g = new_grid()
		for x in range(0, x_len):
			for y in range(0, y_len):
				count = 0
				for n_x in range(x-1,x+2):
					for n_y in range(y-1,y+2):
						#Skip ourselves
						if n_x == x and n_y == y:
							continue
						#Skip out of bounds
						elif n_x < 0 or n_x >= x_len or n_y < 0 or n_y >= y_len:
							continue
						count += g[n_x][n_y]
				#If on
				if g[x][y] == 1:
					value = 1 if count == 2 or count == 3 else 0
				#If off
				else:
					value = 1 if count == 3 else 0
				new_g[x][y] = value
		g = new_g
	#Count on
	count = 0
	for x in range(x_len):
		for y in range(y_len):
			count += g[x][y]
	print count

if __name__ == "__main__":
	main()
