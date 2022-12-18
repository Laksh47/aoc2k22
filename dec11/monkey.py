from collections import deque

# could have used match or parse than this but oh well!
def parse_monkey_config(monkey_config):
    monkey_config = monkey_config.split('\n')
    starting_items = monkey_config[1].split(':')[1].strip()
    operation = monkey_config[2].split(':')[1].strip().split('=')[1].strip()

    test = monkey_config[3].split(':')[1].strip()
    test = test.split()[-1]
    
    test_true = monkey_config[4].split(':')[1].strip()
    test_true = test_true.split()[-1]
    
    test_false = monkey_config[5].split(':')[1].strip()
    test_false = test_false.split()[-1]

    return [int(i) for i in starting_items.split(',')], operation, int(test), int(test_true), int(test_false)

class Monkey(object):
    def __init__(self, items, expr, divide_by, true_monkey, false_monkey):
        self.items = deque(items)
        self.expr = expr
        self.divide_by = divide_by
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def eval_expr(self, old):
        result = eval(self.expr)
        return result

    def test(self, value):
        if value % self.divide_by == 0:
            return self.true_monkey
        return self.false_monkey

def print_monkey_items(monkeys):
    for i, monkey in enumerate(monkeys):
        print(i, monkey.items)

def process_input(path = './input_test.txt', rounds = 20, manage_worry = True):
  with open(path) as fp:
    monkey_configs = fp.read().split("\n\n")
    # print(monkey_configs, len(monkey_configs))

    all_prod = 1
    monkeys = []
    for m in monkey_configs:
        parsed = parse_monkey_config(m)
        all_prod *= parsed[2]
        monkeys.append(Monkey(*parsed))

    monkey_inspects = [0] * len(monkeys)

    for _ in range(rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            # print(monkey_num)
            while monkey.items:
                monkey_inspects[i] += 1
                item = monkey.items.popleft()
                worry_level = monkey.eval_expr(item)

                if manage_worry:
                  worry_level = worry_level // 3
                worry_level = worry_level % all_prod
                next_monkey = monkey.test(worry_level)
                monkeys[next_monkey].items.append(worry_level)

        # print("After round:", _)
        # print_monkey_items(monkeys)
        # print()
  return sorted(monkey_inspects)

sol1 = process_input('input.txt')
print(sol1)

sol2 = process_input('input.txt', 10000, False)
print(sol2)