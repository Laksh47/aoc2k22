import copy

def split_input(lines):
    # print(lines)
    i = lines.index('')
    return(lines[:i], lines[i+1:])

def get_stacks(stack_lines):
    total_stacks = (len(stack_lines[0]) // 4) + 1
    parsed = [[] for _ in range(total_stacks)]

    # print(stacks)
    # print(total_stacks)
    for line in reversed(stack_lines):
        # print(line, len(line))
        for i, c in enumerate(line):
            # print(i, c)
            if c.isalpha():
                parsed[(i // 4)].append(c)

    # print(parsed)
    return parsed

def get_moves(move_lines):
    moves = []
    for line in move_lines:
        temp = map(int, filter(lambda x: x.isnumeric() , line.split()))
        moves.append(tuple(temp))

    # [(qty, src, dest)]
    # print(moves)
    return moves

def crane_it_9000(stacks, qty, src, dest):
    popped = []
    for _ in range(qty):
        popped.append(stacks[src - 1].pop())
    stacks[dest - 1].extend(popped)

def crane_it_9001(stacks, qty, src, dest):
    popped = []
    for _ in range(qty):
        popped.append(stacks[src - 1].pop())
    stacks[dest - 1].extend(reversed(popped))

path = './input.txt'
with open(path) as fp:
    all_lines = fp.read().splitlines() #readlines()
    stack_lines, move_lines = split_input(all_lines)

    stacks = get_stacks(stack_lines)
    moves = get_moves(move_lines)

    stacks_2 = copy.deepcopy(stacks)

    # part 1
    for move in moves:
        crane_it_9000(stacks, *move)

    ans = [stack[-1] for stack in stacks]
    ans = ''.join(ans)
    print(ans)

    # part 2
    for move in moves:
        crane_it_9001(stacks_2, *move)

    ans = [stack[-1] for stack in stacks_2]
    ans = ''.join(ans)
    print(ans)