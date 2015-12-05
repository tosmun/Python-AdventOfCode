import re

def findFirst(pattern, line):
	return next(pattern.finditer(line), None)

VOWEL_PATTERN=re.compile(r'a|e|i|o|u')
VOWEL_MIN=3
DOUBLE_CHAR_PATTERN=re.compile(r'([A-Za-z])\1{1,}')
INVALID_SEQ_PATTERN=re.compile(r'(?:ab|cd|pq|xy)')

nice_count=0
with open('../input.txt','r') as fp:
	while True:
		line = fp.readline()
		if line is None or line == '':
			break
		line = line.strip()
		if line == '':
			continue
		#Contains at least one double char
		doubleMatch = findFirst(DOUBLE_CHAR_PATTERN, line)
		if doubleMatch is None or len(doubleMatch.groups()) < 0:
			continue
		#Contains any invalid sequences of chars
		if findFirst(INVALID_SEQ_PATTERN, line) is not None:
			continue
		#Total number of vowels
		if len(tuple(VOWEL_PATTERN.findall(line))) < VOWEL_MIN:
			continue
		nice_count += 1
print('nice_count: %d' % nice_count)
