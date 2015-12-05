total_wrapping_area=0
total_ribbon_length=0
with open('../input.txt','r') as fp:
	while(True):
		line = fp.readline()
		if line == '':
			break
		line=line.strip()
		if line == '':
			continue
		(l,w,h) = [int(x) for x in line.split('x')]
		#area
		area = 2*l*w + 2*w*h + 2*h*l
		#slack
		(small,medium,large) = sorted([l,w,h])
		slack = small*medium
		#total_wrapping_area
		total_wrapping_area += area + slack
		#ribbon
		ribbon = (small+small+medium+medium)
		bow = (l*w*h)
		total_ribbon_length += ribbon + bow
print('total_wrapping_area: %d' % total_wrapping_area)
print('total_ribbon_length: %d' % total_ribbon_length)
