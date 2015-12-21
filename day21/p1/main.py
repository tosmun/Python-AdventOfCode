from itertools import combinations

START_P_HP = 100
START_P_DMG = 0
START_P_A = 0

START_B_HP = 100
START_B_DMG = 8
START_B_A = 2

WEAPONS = [ [8,4,0], [10,5,0], [25,6,0], [40,7,0], [74,8,0] ]
ARMOR = [ [13,0,1], [31,0,2], [53,0,3], [75,0,4], [102,0,5] ]
#Include 'no armor' option
ARMOR.append([0,0,0])
RINGS = [ [25,1,0], [50,2,0], [100,3,0], [20,0,1], [40,0,2], [80,0,3] ]
#Include 'no ring' options
RINGS.append([0,0,0])
RINGS.append([0,0,0])

def main():
	cost = None
	#1 Weapon
	for w in combinations(WEAPONS, 1):
		#0-1 Armor
		for a in combinations(ARMOR, 1):
			#0-2 Rings
			for r in combinations(RINGS, 2):
				bonuses = calc_bonuses(w,a,r)
				p_hp = START_P_HP
				p_cost = bonuses[0]
				p_dmg = bonuses[1] + START_P_DMG
				p_a = bonuses[2] + START_P_A
				win = is_win(START_B_HP, START_B_DMG, START_B_A, p_hp, p_dmg, p_a)
				if win and (cost is None or p_cost < cost):
					cost = p_cost
	print cost
def is_win(b_hp, b_dmg, b_a, p_hp, p_dmg, p_a):
	b_dmg = max(b_dmg - p_a, 1)
	p_dmg = max(p_dmg - b_a, 1)
	#<= because we start first
	return (b_hp / p_dmg) <= (p_hp / b_dmg)
def calc_bonuses(w,a,r):
	ret = [0, 0, 0]
	for i in [w,a,r]:
		for j in i:	
			ret[0] += j[0]
			ret[1] += j[1]
			ret[2] += j[2]
	return ret

if __name__ == "__main__":
	main()
