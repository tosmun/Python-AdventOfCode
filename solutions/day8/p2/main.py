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
			line = re.sub(r'("|\\)', r'\\\1', line)
			#Surround in quotes
			line = '"%s"' % line
			count += len(line) - orig
		print count
