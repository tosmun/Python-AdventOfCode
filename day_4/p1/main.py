import md5

secret = 'ckczppom'
starts_with = '00000'
starts_with_l = len(starts_with)
index=1
while(True):
	hash=md5.new("%s%d"%(secret,index)).hexdigest()
	if hash[0:starts_with_l] == starts_with:
		break
	index += 1
print(index)
