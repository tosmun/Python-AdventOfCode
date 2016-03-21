import re

#This solution is fairly generic.
#We could assume there are always only 3 items, but that wouldn't be fun

SP = re.compile(r'^Sue ([0-9]+)')
P = re.compile(r'(\w+): ([0-9]+)')
ITEMS = {'children':'==3','cats':'>7','samoyeds':'==2','pomeranians':'<3','akitas':'==0','vizslas':'==0','goldfish':'<5','trees':'>3','cars':'==2','perfumes':'==1'}
if __name__ == "__main__":
	best_match = (-1, None, None)
	with open('../input.txt', 'r') as fp:
		while True:
			line = fp.readline()
			if line is None or line == '':
				break
			sue = int(SP.match(line).group(1))
			items = { }
			match_count = 0
			for match in P.finditer(line):
				name = match.group(1).strip().lower()
				count = int(match.group(2))
				if name in ITEMS and eval('%d%s' % (count, ITEMS[name])):
					match_count += 1
				items[name] = count
			if match_count >= best_match[0]:
				best_match = (match_count, sue, items)
	print best_match
