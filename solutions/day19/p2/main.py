
def get_calibration():
	with open('../calibration.txt', 'r') as fp:
		return fp.read().strip()

def get_replacements():
	r = [ ]
	with open('../replacements.txt', 'r') as fp:
		while True:
			line = fp.readline()
			if line is None or line == '':
				break
			parts = line.split(' ')
			r.append((parts[0].strip(), parts[2].strip()))
	return r

def main():
	c = get_calibration()
	r = get_replacements()
	steps = 0
	prev_steps = -1
	#This solution assumes there is one and only one path to e
	#In which case we don't have to account for multiple paths, and
	#can just iterate through the replacements until e is found
	while c != 'e' and prev_steps != steps:
		prev_steps = steps
		for rs, rt in r:
			for i in range(len(c)):
				if rt == c[i:i+len(rt)]:
					c = c[:i] + rs + c[i+len(rt):]
					steps += 1
					break
	if c != 'e':
		raise Exception("No solution")
	print steps

if __name__ == "__main__":
	main()
