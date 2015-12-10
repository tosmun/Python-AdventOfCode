
input="1113222113"
iterations=50
if __name__ == "__main__":
	output = input
	for i in range(0, iterations):
		count = 0
		prev = None
		new = ""
		for i, c in enumerate(output):
			#First char
			if prev is None:
				prev = c
				count += 1
			else:
				#Same char
				if prev == c:
					count += 1
				#New char
				else:
					new += "%d%s" %(count, prev)
					prev = c
					count = 1
			#Last char
                        if i == len(output)-1:
                                new += "%d%s" %(count, prev)
		output = new
	print len(output)
