from collections import defaultdict
from math import prod

def parse_input(path = './input_test.txt'):
    data = []
    with open(path) as fp:
        for line in fp.read().splitlines():
            data.append([int(x) for x in list(line)])

    return data

# 30373
# 25512
# 65332
# 33549
# 35390
def visible_trees(data):
    def dfs(data, i, j):
        if i == 0 or j == 0 or i == len(data) - 1 or j == len(data[0]) - 1:
            return True, 0

        curr_value = data[i][j]

        up, down, left, right = True, True, True, True
        scenic_score = defaultdict(int)

        temp = i - 1
        while temp >= 0:
            scenic_score['up'] += 1
            if curr_value <= data[temp][j]:
                up = False
                break
            temp -= 1

        temp = i + 1
        while temp < len(data):
            scenic_score['down'] += 1
            if curr_value <= data[temp][j]:
                down = False
                break
            temp += 1
        
        temp = j - 1
        while temp >= 0:
            scenic_score['left'] += 1
            if curr_value <= data[i][temp]:
                left = False
                break
            temp -= 1

        temp = j + 1
        while temp < len(data[0]):
            scenic_score['right'] += 1
            if curr_value <= data[i][temp]:
                right = False
                break
            temp += 1

        curr_score = prod(list(scenic_score.values()))
        # print(i, j, curr_value, curr_score, scenic_score)

        if up or down or left or right:
            return (True, curr_score)
        
        return (False, curr_score)

    count = 0
    max_scenic_score = float('-inf')
    for i in range(len(data)):
        for j in range(len(data[0])):
            visible, curr_score = dfs(data, i, j)
            max_scenic_score = max(max_scenic_score, curr_score)
            if visible:
                count += 1

    return count, max_scenic_score


data = parse_input('./input.txt')
# data = parse_input()
# print(data)
count = visible_trees(data)
print(count)