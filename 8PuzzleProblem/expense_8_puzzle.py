import copy
import sys


inFile = sys.argv[1]
outFile = sys.argv[2]
function = sys.argv[3]
flag = sys.argv[4]


def dumpfile(fringe, closed):
    outF = open("DumpFile.txt", "w")
    outF.write("Fringe")
    outF.write(str(fringe))
    outF.write("\n")
    outF.write("Closed")
    outF.write(str(closed))
    outF.write("\n")
    outF.close()


def readfile(filename):
    with open(filename, 'r') as file:
        arr = [list(map(int, line.split())) for line in file if line.strip() != "END OF FILE"]
    return arr


class Node:
    def __init__(self, parent, data, cost):
        self.parent = parent
        self.data = data
        self.cost = cost


initial_state = readfile(inFile)
goal_state = readfile(outFile)
n = Node([], initial_state, 0)


def min_index(arr):
    return arr.index(min(arr))


def empty_space(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def expand_node(node):
    arr = []
    cost = []
    x, y = empty_space(node)
    if x > 0:
        state = copy.deepcopy(node)
        state[x][y] = state[x-1][y]
        state[x-1][y] = 0
        c = state[x][y]
        cost.append(c)
        arr.append(state)
    if x < 2:
        state = copy.deepcopy(node)
        state[x][y] = state[x+1][y]
        state[x + 1][y] = 0
        c = state[x][y]
        cost.append(c)
        arr.append(state)
    if y > 0:
        state = copy.deepcopy(node)
        state[x][y] = state[x][y - 1]
        state[x][y - 1] = 0
        c = state[x][y]
        cost.append(c)
        arr.append(state)
    if y < 2:
        state = copy.deepcopy(node)
        state[x][y] = state[x][y + 1]
        state[x][y + 1] = 0
        c = state[x][y]
        cost.append(c)
        arr.append(state)
    return arr, cost


def cost(lis, cos):
    dict_cost = {}
    for i in range(len(cos)):
        x = str(cos[i])
        dict_cost[x] = lis[i]
    return dict_cost


def bfs(ins, gls, Dumpflag):
    fringe = [ins]
    count = 1
    node_popped = 0
    closed = []
    while count < 50000:
        if fringe is []:
            print('Search Failed')
        parent = fringe.pop(0)
        node_popped += 1
        if gls == parent:
            print("Solution Found")
            break
        if parent not in closed:
            closed.append(parent)
            new_nodes, co = expand_node(parent)
            d = cost(new_nodes, co)
            for i in new_nodes:
                fringe.append(i)
        count += 1
    if Dumpflag == "true":
        dumpfile(fringe, closed)
    print("node_popped")
    print(node_popped)


def dfs(ins, gls, Dumpflag):
    fringe = [ins]
    count = 1
    node_popped = 0
    closed = []
    while count < 50000:
        if fringe is []:
            print('Search Failed')
        parent = fringe.pop(-1)
        node_popped += 1
        if gls == parent:
            print("Solution Found")
            break
        if parent not in closed:
            closed.append(parent)
            new_nodes, co = expand_node(parent)
            d = cost(new_nodes, co)
            for i in new_nodes:
                fringe.append(i)
        count += 1
    if Dumpflag == "true":
        dumpfile(fringe, closed)
    print("node_popped")
    print(node_popped)


def ucs(ins, gls, Dumpflag):
    fringe = [ins]
    count = 1
    node_popped = 0
    closed = []
    while count != 0:
        if fringe is []:
            print('Search Failed')
        index = index(min(co))
        # d = cost(new_nodes, co)
        parent = fringe.pop(index)
        node_popped += 1
        if gls == parent:
            print("Solution Found")
            break
        if parent not in closed:
            closed.append(parent)
            new_nodes, co = expand_node(parent)
            for i in new_nodes:
                fringe.append(i)
            # d = cost(new_nodes, co)
            # print(d)
        count += 1
    if Dumpflag == "true":
        dumpfile(fringe, closed)
    print("node_popped")
    print(node_popped)


def dls(ins, gls, Dumpflag):
    fringe = [ins]
    count = 1
    dls = 1
    node_popped = 0
    closed = []
    while count < dls:
        if fringe is []:
            print('Search Failed')
        parent = fringe.pop(0)
        node_popped += 1
        if gls == parent:
            print("Solution Found")
            break
        if parent not in closed:
            closed.append(parent)
            new_nodes, co = expand_node(parent)
            # d = cost(new_nodes, co)
            for i in new_nodes:
                fringe.append(i)
        count += 1
        dls += 1
    if Dumpflag == "true":
        dumpfile(fringe, closed)
    print("node_popped")
    print(node_popped)


def ids(ins, gls, Dumpflag):
    fringe = [ins]
    count = 1
    node_popped = 0
    closed = []
    ids = 0
    while count != 0:
        if fringe is []:
            print('Search Failed')
        parent = fringe.pop(-1)
        node_popped += 1
        if gls == parent:
            print("Solution Found")
            break
        if parent not in closed:
            closed.append(parent)
            new_nodes, co = expand_node(parent)
            d = cost(new_nodes, co)
            for i in new_nodes:
                fringe.append(i)
    count += 1
    ids += 5
    if Dumpflag == "true":
        dumpfile(fringe, closed)
    print("node_popped")
    print(node_popped)


def greedy(ins, gls, Dumpflag):
    fringe = [ins]
    count = 1
    node_popped = 0
    closed = []
    while count != 0:
        if fringe is []:
            print('Search Failed')
        # d = cost(new_nodes, co)
        parent = fringe.pop(0)
        node_popped += 1
        if gls == parent:
            print("Solution Found")
            break
        if parent not in closed:
            closed.append(parent)
            new_nodes, co = expand_node(parent)
            ind = min_index(co)
            for i in new_nodes:
                fringe.append(i)
        count += 1
    if Dumpflag == "true":
        dumpfile(fringe, closed)
    print("node_popped")
    print(node_popped)


def astar(ins, gls, Dumpflag):
    fringe = [ins]
    count = 1
    node_popped = 0
    closed = []
    while count < 50000:
        if fringe is []:
            print('Search Failed')
        parent = fringe.pop(0)
        node_popped += 1
        if gls == parent:
            print("Solution Found")
            break
        if parent not in closed:
            closed.append(parent)
            new_nodes, co = expand_node(parent)
            d = cost(new_nodes, co)
            for i in new_nodes:
                fringe.append(i)
        count += 1
    if Dumpflag == "true":
        dumpfile(fringe, closed)
    print("node_popped")
    print(node_popped)


match function:
    case "bfs":
        bfs(initial_state, goal_state, flag)
    case "dfs":
        dfs(initial_state, goal_state, flag)
    case "ucs":
        ucs(initial_state, goal_state, flag)
    case "dls":
        dls(initial_state, goal_state, flag)
    case "ids":
        ids(initial_state, goal_state, flag)
    case "greedy":
        greedy(initial_state, goal_state, flag)
    case "astar":
        astar(initial_state, goal_state, flag)
