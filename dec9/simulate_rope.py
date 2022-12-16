
# point obj, can be a tuple
# three obj, s, H, T
# is adjacent, is on the same row/col
# track unique tail position during movement

def is_touching(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        return True
    return False

def is_collinear(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 or y1 == y2:
        return True
    return False

def process_input(path = './input_test.txt', num = 2):
    points = [[0, 0] for _ in range(num)]
    visited = set()

    def move_straight(point, direction):
        if direction == 'R':
            point[0] += 1
        elif direction == 'L':
            point[0] -= 1
        elif direction == 'U':
            point[1] += 1
        elif direction == 'D':
            point[1] -= 1

    def move_diagonal(point, direction):
        if direction == 'RU':
            move_straight(point, 'R')
            move_straight(point, 'U')
        elif direction == 'RD':
            move_straight(point, 'R')
            move_straight(point, 'D')
        elif direction == 'LU':
            move_straight(point, 'L')
            move_straight(point, 'U')
        elif direction == 'LD':
            move_straight(point, 'L')
            move_straight(point, 'D')
            
    def move(line):
        direction, steps = line.split()
        print(line)
        print("head:", points[0], " tail:", points[-1])
        print("moves start")

        for _ in range(int(steps)):
            head = points[0]
            move_straight(head, direction)

            for i in range(len(points) - 1):
                curr_head = points[i]
                curr_tail = points[i + 1]

                # # alternate logic to move straight and diagonal
                # x1, y1 = curr_tail
                # x2, y2 = curr_head
                # dx, dy = (x2 - x1), (y2 - y1)
                # if max(abs(dx),abs(dy)) > 1:
                #     diffx, diffy = min(max(dx, -1), 1), min(max(dy, -1), 1)
                #     curr_tail[0] += diffx
                #     curr_tail[1] += diffy
                
                x1, y1 = curr_tail
                x2, y2 = curr_head
                if not is_touching(curr_head, curr_tail) and not is_collinear(curr_head, curr_tail):
                    if x1 < x2 and y1 < y2:
                        move_diagonal(curr_tail, 'RU')
                    elif x1 < x2 and y2 < y1:
                        move_diagonal(curr_tail, 'RD')
                    elif x1 > x2 and y1 < y2:
                        move_diagonal(curr_tail, 'LU')
                    elif x1 > x2 and y2 < y1:
                        move_diagonal(curr_tail, 'LD')
                elif not is_touching(curr_head, curr_tail) and is_collinear(curr_head, curr_tail):
                    if x1 < x2:
                        move_straight(curr_tail, 'R')
                    elif x1 > x2:
                        move_straight(curr_tail, 'L')
                    if y1 < y2:
                        move_straight(curr_tail, 'U')
                    elif y1 > y2:
                        move_straight(curr_tail, 'D')

                visited.add(tuple(points[-1]))

        
        print("head:", points[0], " tail:", points[-1])
        print("moves end")
        print()

    with open(path) as fp:
        for line in fp.read().splitlines():            
            move(line)

    print(visited)
    return len(visited)

sol1 = process_input('./input.txt', 2)
sol2 = process_input('./input.txt', 10)
print(sol1, sol2)