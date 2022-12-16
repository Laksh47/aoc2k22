def process_input(path = './input_test.txt'):
  cycle = 1
  x = 1

  cycle_tracker = 20
  total_strength = 0

  strength = {}

  def process_line(line):
    nonlocal cycle, x, total_strength, cycle_tracker

    op, value = line[:4], line[5:]
    # print(op, value)
    # curr_strength = cycle * x
    # print(cycle, cycle_tracker, x, curr_strength, total_strength)
    # print()

    # if cycle == cycle_tracker:
    #   total_strength += curr_strength
    #   cycle_tracker += 40

    if op == 'noop':
      strength[cycle] = x
      cycle += 1
    elif op == 'addx':
      value = int(value.strip())
      strength[cycle] = x
      strength[cycle + 1] = x
      x += value
      cycle += 2

  with open(path) as fp:
    for line in fp.read().splitlines():
      process_line(line)

  print(strength)
  print()

  for cycle in[20, 60, 100, 140, 180, 220]:
    total_strength += cycle * strength[cycle]

  crts = []
  crt = ''
  for cycle, x in strength.items():
    position = (cycle - 1) % 40
    if x - 1 <= position <= x + 1:
      crt +='#'
    else:
      crt +=' '
    if len(crt) % 40 == 0:
      crts.append(crt)
      crt = ''
  for crt in crts:
    print(crt)
  return total_strength

sol = process_input('input.txt')
# sol = process_input()
print(sol)