class Node(object):
    def __init__(self, name, parent = None, size = 0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []

    def add_child(self, child: "Node"):
        self.children.append(child)

    def custom_size(self):
        return self.size + sum([child.custom_size() for child in self.children])

    def __str__(self) -> str:
        return f"{self.name}, {self.size}, {self.parent}, {self.children}"

def get_cmds(lines):
    cmds, output = [], []
    for line in lines:
        if line.startswith('$'):
            if output:
                cmds.append(output)
            output = line[1:].strip().split()
        else:
            output.append(line.strip())

    if output:
        cmds.append(output)
    
    return cmds

def get_tree(cmds):
    root = Node('/')
    dir_nodes = [root]
    
    node = root
    for cmd in cmds:
        # print(cmd)
        if cmd[0] == 'ls':
            children = cmd[1:]
            for child in children:
                if child.startswith('dir'):
                    dir_name = child.split()[1]
                    new_dir = Node(dir_name, node)
                    node.add_child(new_dir)
                else:
                    size, filename = child.split()

                    # # skipping adding files to node struct
                    file = Node(filename, node, int(size))
                    node.add_child(file)
        else:
            dir = cmd[1]
            if dir == '..':
                node = node.parent
            elif dir != '/':
                new_dir = Node(dir, node)
                dir_nodes.append(new_dir)
                node.add_child(new_dir)
                node = new_dir

    return root, dir_nodes

path = './input.txt'
with open(path) as fp:
    lines = fp.read().splitlines()
    cmds = get_cmds(lines)
    root, dir_nodes = get_tree(cmds)

    # print()
    # print(root)
    # print()

    dir_tuples = []
    total = 0
    for dir in dir_nodes:
        curr_size = dir.custom_size()
        dir_tuples.append((curr_size, dir.name))
        # print(dir.name, curr_size)
        if curr_size < 100000:
            total += curr_size
    # part a
    print(total)

    # print(dir_tuples)
    root_size, _ = dir_tuples[0]

    max_size = 70000000
    free_size = max_size - root_size
    size_needed = 30000000 - free_size

    dir_tuples.sort()
    for (curr_size, name) in dir_tuples:
        if curr_size > size_needed:
            # part b
            print(name, curr_size)
            break
