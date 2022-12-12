def is_fully_contained(range1, range2):
    x1, y1 = tuple([int(r) for r in range1.split('-')])
    x2, y2 = tuple([int(r) for r in range2.split('-')])

    if x2 <= x1 <= y2 or x2 <= y1 <= y2: # and -> or
        return True

    if x1 <= x2 <= y1 or x1 <= y2 <= y1: # and -> or
        return True
    
    return False

path = './input.txt'

total = 0
with open(path) as fp:
   for line in fp:
    range1, range2 = line.split(',')
    if is_fully_contained(range1, range2):
        total += 1

print(total)