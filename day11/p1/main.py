import copy, re

encoding="UTF-8"
input=bytearray('hepxcrrq',encoding)
max_byte=bytearray('z', encoding)[0]
min_byte=bytearray('a', encoding)[0]
invalid_chars=bytearray('iol', encoding)
double_char_pattern=re.compile(r'(.|^)(?!\1)(.)\2(?!\2)')

new=copy.copy(input)
while True:
	#Work backwards
	for i in range(len(new)-1,-1,-1):
		if new[i] == max_byte:
			new[i] = min_byte
			#Detect rollover
			if i == 0:
				#TODO more pythonic way?
				for i in range(0, len(new)):
					new[i] = min_byte
				break
		else:
			new[i] = new[i] + 1
			#Ensure valid char
			while(new[i] in invalid_chars):
				new[i] = new[i] + 1
			break
	#Check for two overlapping pairs
	new_str = new.decode(encoding)
	if len(double_char_pattern.findall(new_str)) < 2:
		continue
	buffer = [ new[0] ]
	for i in range(1, len(new)):
		if len(buffer) == 3:
			break
		elif buffer[-1] != new[i]-1:
			buffer = [ new[i] ]
		else:
			buffer.append(new[i])
	if len(buffer) == 3:
		print(new.decode(encoding))
		break
	if new == input:
		raise Exception("No suitable new password found")
