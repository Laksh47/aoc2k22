def process_input(path = './input_test.txt'):
  def process_line(line):
    print(line)

  with open(path) as fp:
    for line in fp.read().splitlines():
      process_line(line)

  return None

sol = process_input()
print(sol)