import json, numbers, sys

sys.setrecursionlimit(10000)

def countJsonNumbers(o):
	ot = type(o)
	#Looking for numbers
	if ot in (int, float, long):
		return o
	#Iterable?
	elif ot in (dict, list):
		#If it is a dictionary, we are only concerned with iterating values
		if ot is dict:
			#If any immediate value in the obj is 'red' we disregard it
			o = o.values()
			if 'red' in o:
				return 0
		count = 0
		for io in o:
			count += countJsonNumbers(io)
		return count
	#All other types
	return 0

if __name__ == '__main__':
	with open('../input.txt', 'r') as fp:
		jobj = json.loads(fp.readline())
	print(countJsonNumbers(jobj))
