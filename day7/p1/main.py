from functools import partial

def resolve(source_str=None):
	try:
		return int(source_str)
	except ValueError:
		obj = c[source_str]
		#If we have not resolved it yet, call it now
		if hasattr(obj, '__call__'):
			c[source_str] = c[source_str]()
		return c[source_str]

def lshift(left=None, right=None):
	return left() << right()
def rshift(left=None, right=None):
	return left() >> right()
def orop(left=None, right=None):
	return left() | right()
def andop(left=None, right=None):
	return left() & right()
def notop(left=None):
	return ~ left()

if __name__ == '__main__':
	c={ }
	with open('../input.txt', 'r') as fp:
		for line in [line.strip() for line in fp if line != '']:
			parts=line.split(' ')
			parts_l=len(parts)
			target=parts[-1]
			source=partial(resolve, source_str=parts[-3])
			#Direct source assignment
			if parts_l == 3:
				c[target]=source
			#Single source
			elif parts_l == 4:
				op=parts[-4]
				if op == 'NOT':
					c[target]=partial(notop, left=source)
			#Two sources
			elif parts_l == 5:
				op=parts[-4]
				source2=partial(resolve, source_str=parts[-5])
				if op == 'LSHIFT':
					c[target]=partial(lshift, left=source2, right=source)
				elif op == 'RSHIFT':
					c[target]=partial(rshift, left=source2, right=source)
				elif op == 'OR':
					c[target]=partial(orop, left=source2, right=source)
				elif op == 'AND':
					c[target]=partial(andop, left=source2, right=source)
	print(c['a']())
