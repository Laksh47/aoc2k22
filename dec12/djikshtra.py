from collections import defaultdict
import heapq

def adj_list(matrix):
    row = len(matrix)
    col = len(matrix[0])

    adj = defaultdict(list)
    for i in range(row):
        for j in range(col):
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + x < row and 0 <= j + y < col:
                    curr_signal = matrix[i][j]
                    next_signal = matrix[i + x][j + y]
                    
                    if ord(next_signal) - ord(curr_signal) <= 1:
                        adj[(i, j)].append((i + x, j + y))

    return adj

def get_pos(matrix):
    row = len(matrix)
    col = len(matrix[0])
    pos = {}
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 'S':
                pos['start'] = (i, j)
            elif matrix[i][j] == 'E':
                pos['end'] = (i, j)

    return pos

def get_all_start(matrix):
    row = len(matrix)
    col = len(matrix[0])
    positions = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 'a':
                positions.append((i, j))

    return positions

# djikshtra shortest path algo
def djikshtra(edges, start, dest):
    visit = set()
    min_heap = [(0, start)]
    
    while min_heap:
        c1, pos1 = heapq.heappop(min_heap)
        if pos1 in visit:
            continue

        if pos1 == dest:
            # print("destination found")
            # print(pos1, c1)
            return c1

        visit.add(pos1)

        for pos2 in edges[pos1]:
            if pos2 not in visit:
                heapq.heappush(min_heap, (c1 + 1, pos2))

    # no way to reach dest, all paths explored
    return float('inf')


def process_input(path = './input_test.txt'):

  with open(path) as fp:
    content = fp.read()
    matrix = [list(row) for row in content.strip().split('\n')]

    pos = get_pos(matrix)

    x, y = pos['start']
    matrix[x][y] = 'a'
    x, y = pos['end']
    matrix[x][y] = 'z'

    adj = adj_list(matrix)

    # sol 1
    # cost = djikshtra(adj, pos['start'], pos['end'])
    # print(cost)

    positions = get_all_start(matrix)
    # print(positions)

    costs = defaultdict(int)
    min_cost = float('inf')
    for start in positions:
        costs[start] = djikshtra(adj, start, pos['end'])
        min_cost = min(min_cost, costs[start])

  return min_cost

sol = process_input('input.txt')
print(sol)
