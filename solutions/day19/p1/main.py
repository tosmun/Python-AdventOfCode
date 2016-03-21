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
	c_matches = set()
	for (rs, rt) in r:
		for i in range(len(c)):
			if rs == c[i:i+len(rs)]:
				c_matches.add(c[:i] + rt + c[i+len(rs):])
	print len(c_matches)	
if __name__ == "__main__":
	main()
