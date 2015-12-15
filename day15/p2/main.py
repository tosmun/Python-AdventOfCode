from itertools import product

if __name__ == '__main__':
	ingredients = [ ]
	with open('../input.txt', 'r') as fp:
		while True:
			line = fp.readline()
			if line is None or line == '':
				break
			parts = line.split(' ')
			name = parts[0].split(':')[0]
			capacity = int(parts[2].split(',')[0])
			durability = int(parts[4].split(',')[0])
			flavor = int(parts[6].split(',')[0])
			texture = int(parts[8].split(',')[0])
			calories = int(parts[10])
			ingredients.append((name, capacity, durability, flavor, texture, calories))
	#Generate ranges to pass into product function
	ranges = [ ]
	for i in range(0, len(ingredients)):
		ranges.append(range(0,100))
	best_score = (-1, None)
	#For every possible combination of ingredients
	for amounts in product(*ranges):
		total_amount = 0
		for amount in amounts:
			total_amount += amount
		#Must amount to 100 - #TODO Surely there is a better way?
		if total_amount != 100:
			continue
		total_calories = 0
		total_capacity = 0
		total_durability = 0
		total_flavor = 0
		total_texture = 0
		for i, ingredient in enumerate(ingredients):
			amount = amounts[i]
			total_calories += (amount * ingredient[5])
			#Break early if already over limit
			if total_calories > 500:
				break
			total_capacity += (amount * ingredient[1])
			total_durability += (amount * ingredient[2])
			total_flavor += (amount * ingredient[3])
			total_texture += (amount * ingredient[4])
		#Calories must be exactly 500
		if total_calories != 500:
			continue
		#We can assume score will be 0
                if total_capacity < 0 or total_durability < 0 or total_flavor < 0 or total_texture < 0:
                        continue
		total_score = total_capacity * total_durability * total_flavor * total_texture
		if total_score > best_score[0]:
			best_score = (total_score, amounts)
	print best_score
