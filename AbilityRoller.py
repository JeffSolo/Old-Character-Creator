from random import randint


def standard():
	for i in xrange(6):
		roll =  [randint(1,6) for j in range(1,5)]
		#print roll
		roll.remove(min(roll))
		#print roll
		print sum(roll)
		
def rerollOnes():
	for i in xrange(6):
		roll =  [randint(2,6) for j in range(1,5)]
		#print roll
		roll.remove(min(roll))
		#print roll
		print sum(roll)

#if rerollOnes = true, a die can't be less than 2
# if bumpHighest = 1, the highest attribute number is bumped to 18
# if bumpLow = 1, no attribute scores are less than 10

def roll(rerollOnes, bumpHighest, bumpLow):
	total = []
	for i in xrange(6):
		if(rerollOnes):
			roll =  [randint(2,6) for j in range(1,5)]
		else:
			roll =  [randint(1,6) for j in range(1,5)]
		roll.remove(min(roll))
		#print roll
		total.append(sum(roll))
		if(bumpLow):
			if total[i] < 10:
				total[i] = 10
	if(bumpHighest):
		total.remove(max(total))
		total.append(18)
	return total
