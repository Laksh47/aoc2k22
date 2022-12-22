from functools import cmp_to_key

def is_right_order(left: list, right: list):
    if type(left) == list and type(right) == int:
      return is_right_order(left, [right])
    elif type(left) == int and type(right) == list:
      return is_right_order([left], right)
    if type(left) == int and type(right) == int:
      return left < right if left != right else None
    else: # both lists
      for sub_left, sub_right in zip(left, right):
        curr = is_right_order(sub_left, sub_right)
        if curr is None:
          continue
        return curr

      return len(left) < len(right) if len(left) != len(right) else None

def comparator(l, r):
  if is_right_order(l, r):
    return -1
  else:
    return 1

# print(is_right_order([1,1,3,1,1], [1,1,5,1,1]))
# print(is_right_order([[1],[2,3,4]], [[1],4]))
# print(is_right_order([9], [[8,7,6]]))
# print(is_right_order([[4,4],4,4], [[4,4],4,4,4]))
# print(is_right_order([7,7,7,7], [7,7,7]))
# print(is_right_order([], [3]))
# print(is_right_order([[[]]], [[]]))
# print(is_right_order([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))

def process_input(path = './input_test.txt'):
  def process_pair(pair):
    # print(pair)
    # print()
    # print(pair.strip().split("\n"))
    # print()
    list1, list2 = pair.strip().split("\n")
    list1 = eval(list1)
    list2 = eval(list2)

    return is_right_order(list1, list2)

  with open(path) as fp:
    contents = fp.read()
    ordered_pairs = [eval(list) for list in contents.split("\n") if list != ''] + [[[2]], [[6]]]
    ordered_pairs = sorted(ordered_pairs, key=cmp_to_key(comparator))
    # print(ordered_pairs)
    pairs = contents.split("\n\n")
    sum = 0
    for i, pair in enumerate(pairs):
        is_ordered = process_pair(pair)
        if is_ordered:
          sum += i + 1

    i1 = ordered_pairs.index([[2]]) + 1
    i2 = ordered_pairs.index([[6]]) + 1
  return sum, i1 * i2

sol = process_input('./input.txt')
print(sol)