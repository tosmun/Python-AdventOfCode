import re

def matches(pattern, line):
	return next(pattern.finditer(line), None) is not None

VOWEL_PATTERN=re.compile(r'(.*[aeiou]){3}')
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
		if not matches(DOUBLE_CHAR_PATTERN, line):
			continue
		#Contains any invalid sequences of chars
		if matches(INVALID_SEQ_PATTERN, line):
			continue
		if not matches(VOWEL_PATTERN, line):
			continue
		nice_count += 1
print('nice_count: %d' % nice_count)
