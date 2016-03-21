from itertools import permutations

if __name__ == "__main__":
	with open('../input.txt', 'r') as fp:
		dists={ }
		while True:
			line=fp.readline()
			if line is None or line == '':
				break
			parts=line.split(" ")
			source=parts[0]
			target=parts[2]
			dist=int(parts[4])
			if source not in dists:
				dists[source] = { }
			dists[source][target] = dist
			if target not in dists:
				dists[target] = { }
			dists[target][source] = dist
	worst_path = None
	#Brute force
	for path in permutations(dists.keys(), len(dists.keys())):
		distance = 0
		for i, source in enumerate(path[0:-1]):
			target=path[i+1]
			#Invalid path if we can not travel this way
			if target not in dists[source]:
				distance = -1
				break
			distance += dists[source][target]
		if distance >= 0 and worst_path is None or distance > worst_path[0]:
			worst_path = (distance, path)
	print worst_path
