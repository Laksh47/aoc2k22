def get_priority(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 1 + 26
    return ord(letter) - ord('a') + 1

def find_intersection_old(rucksack):
    half = len(rucksack) // 2
    comp1, comp2 = rucksack[:half], rucksack[half:]
    return ''.join(set(comp1).intersection(comp2))

def find_intersection(rucksack_group):
    char_set = set.intersection(*map(set, rucksack_group))
    return ''.join(char_set)

path = './input.txt'

total = 0
with open(path) as fp:
    rucksack_group = []
    for rucksack in fp:
        rucksack_group.append(rucksack.strip())

        if len(rucksack_group) % 3 == 0:
            # print(rucksack_group)
            common = find_intersection(rucksack_group)
            # print(common)
            total += get_priority(common)
            rucksack_group = []

print(total)