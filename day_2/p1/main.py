total_area=0
with open('../input.txt','r') as fp:
	while(True):
		line = fp.readline()
		if line == '':
			break
		line = line.strip()
		if line == '':
			continue
		(l,w,h) = [int(x) for x in line.split('x')]
		area = 2*l*w + 2*w*h + 2*h*l
		(s,m,lg) = sorted([l,w,h])
		slack = s*m
		total_area += area + slack
print('total_area: %d' % total_area)
