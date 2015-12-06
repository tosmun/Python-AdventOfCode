import re

def matches(pattern, line):
	return next(pattern.finditer(line), None) is not None

PAIR_PATTERN=re.compile(r'([A-Za-z][A-Za-z]).*\1')
INBETWEEN_CHAR_PATTERN=re.compile(r'([A-Za-z])[A-Za-z]\1')

nice_count=0
with open('../input.txt','r') as fp:
	while True:
		line = fp.readline()
		if line is None or line == '':
			break
		line = line.strip()
		if line == '':
			continue
		if not matches(PAIR_PATTERN, line):
			continue
		if not matches(INBETWEEN_CHAR_PATTERN, line):
			continue
		nice_count += 1
print('nice_count: %d' % nice_count)
