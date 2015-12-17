from itertools import combinations

if __name__ == "__main__":
	bottles = [ ]
	with open('../input.txt', 'r') as fp:
		while True:
			line = fp.readline()
			if line is None or line == "":
				break
			bottles.append(int(line))
	count = 0
	#For each possible sequence length
	for length in range(1, len(bottles)):
		#For each combination of bottles at this length
		for sequence in combinations(bottles, length):
			if sum(sequence) == 150:
				count += 1
	print count
