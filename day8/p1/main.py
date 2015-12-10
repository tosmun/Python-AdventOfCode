import re

if __name__ == "__main__":
	count = 0
	with open('../input.txt', 'r') as fp:
		count = 0
		while True:
			line=fp.readline()
			if line is None or line == '':
				break
			#Remove whitespace
			line=line.strip()
			orig = len(line)
			#This is horribly inefficient, but it's easier than trying to figure out a combined regex
			line = re.sub(r'^"|"$', '', line)
			line = re.sub(r'\\\\', 'E', line)
			line = re.sub(r'\\"', 'E', line)
			line = re.sub(r'\\x..', 'E', line)
			count += orig-len(line)
		print count
