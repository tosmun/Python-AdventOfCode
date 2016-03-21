from itertools import combinations

NUM_BUCKETS = 4

def main():
    ws = [ ]
    [ws.append(int(line)) for line in open('../input.txt')]
    #Sort lowest to highest, just in case
    ws = sorted(ws)
    #The weight we are looking for will be such that all buckets weigh the same
    desired_weight = sum(ws) / NUM_BUCKETS

    #I found that the brute force solution was taking way too long
    #and decided to assume that perhaps the groups were of equal length
    valid_ws = None
    for l in range(1, len(ws)):
        for w in [x for x in combinations(ws,l) if sum(x) == desired_weight]:
            if valid_ws is None:
                valid_ws = [ ]
            valid_ws.append(w)
        if valid_ws is not None:
            break
    #Find smallest QE by multiplying each element in the first set
    smallest_qe_set = min(valid_ws, key=lambda x: reduce(lambda x,y: x*y, x))
    print "Smallest QE: %d" % reduce(lambda x,y: x*y, smallest_qe_set)
if __name__ == '__main__':
    main()