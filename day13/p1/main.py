from itertools import permutations

if __name__ == "__main__":
	map = { }
	with open('../input.txt', 'r') as fp:
		while True:
			line=fp.readline()
			if line is None or line == '':
				break
			parts = line.split(" ")
			person = parts[0]
			value = int(parts[3])
			if parts[2] == 'lose':
				value = value * -1
			neighbour = parts[10].split('.')[0]
			if person not in map:
				map[person] = { }
			person_map = map[person]
			person_map[neighbour] = value
	best = (-1, None)
	#For each possible combination
	for arrangement in permutations(map.keys(), len(map.keys())):
		#Calculate total
		total = 0
		for i, person in enumerate(arrangement):
			#Have to account for boundaries of the list
			left = (i-1 if i > 0 else -1)
			right = (i+1 if i < len(arrangement)-1 else 0)
			total += map[person][arrangement[left]]
			total += map[person][arrangement[right]]
		if total > best[0]:
			best = (total, arrangement)
	print(best)
