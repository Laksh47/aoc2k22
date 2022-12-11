import heapq

ordered_elves = []
path = './input.txt'

curr_calories, max_calories = 0, 0
with open(path) as fp:
   line = fp.readline()

   elf_no = 1
   while line:
    if line == '\n':
        # max_calories = max(max_calories, curr_calories)
        # print(f"{elf_no} has {curr_calories}")
        heapq.heappush(ordered_elves, (-curr_calories, elf_no))
        curr_calories = 0
        elf_no += 1
    else:
        curr_calories += int(line)

    line = fp.readline()


top_elf1 = heapq.heappop(ordered_elves)
top_elf2 = heapq.heappop(ordered_elves)
top_elf3 = heapq.heappop(ordered_elves)

print(f"{top_elf1}, {top_elf2}, {top_elf3}")
print(f"Sum of top3: {-top_elf1[0] + -top_elf2[0] + -top_elf3[0]}")
