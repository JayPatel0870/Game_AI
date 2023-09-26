import copy

initial_state = [[2, 3, 6], [1, 0, 7], [4, 8, 5]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
fringe = [initial_state]
closed = []


def empty_space(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def neighbour_expand(state):
    x, y = empty_space(state)
    n = []
    c = []
    if x > 0:
        ns = copy.deepcopy(state)
        ns[x][y] = ns[x-1][y]
        ns[x-1][y] = 0
        ct = ns[x][y]
        n.append(ns)
        c.append(ct)
    if x < 2:
        ns = copy.deepcopy(state)
        ns[x][y] = ns[x + 1][y]
        ns[x + 1][y] = 0
        ct = ns[x][y]
        n.append(ns)
        c.append(ct)
    if y > 0:
        ns = copy.deepcopy(state)
        ns[x][y] = ns[x][y-1]
        ns[x][y - 1] = 0
        ct = ns[x][y]
        n.append(ns)
        c.append(ct)
    if y < 2:
        ns = copy.deepcopy(state)
        ns[x][y] = ns[x][y+1]
        ns[x][y+1] = 0
        ct = ns[x][y]
        n.append(ns)
        c.append(ct)
    return n, c


def bfs(fringe, gls):
    node_pop = 0
    node_expanded = 0
    count = 0
    cost1 = 0
    while count < 5000:
        if fringe is []:
            print("Search Failed")
        node = fringe.pop(0)
        node_pop += 1
        if gls == node:
            print("Solution Found")
            break
        if node not in closed:
            closed.append(node)
            new_nodes, cost = neighbour_expand(node)
            cost1 = cost1 + sum(cost)
            node_expanded += 1
            for i in new_nodes:
                fringe.append(i)
        count += 1
    print(node_expanded)
    print(node_pop)
    print(count)
    print(cost1)


def dfs(fringe, gls):
    node_pop = 0
    node_expanded = 0
    count = 0
    cost1 = 0
    while count < 50000:
        if fringe is []:
            print("Search Failed")
        node = fringe.pop(-1)
        node_pop += 1
        if gls == node:
            print("Solution Found")
            break
        if node not in closed:
            node_expanded += 1
            closed.append(node)
            new_nodes, cost = neighbour_expand(node)
            cost1 = cost1 + sum(cost)
            for i in new_nodes:
                fringe.append(i)
        count += 1
    print(node_expanded)
    print(node_pop)
    print(count)
    print(cost1)


def ucs(fringe, gls):






    # count = 0
    # if f is not [] and f[0] == gls:
    #     print("Solution Found")
    # else:
    #         nodes = neighbour_expand(f[0])
    #         for i in nodes:
    #             if i is not None:
    #                 f.append(i)
    #         closed.add(tuple(map(tuple, f.pop(0))))
    #         print("fringe")
    #         print(f[0])
    #         print("closed")
    #         print(closed)
    #         # bfs(f, gls)


    # fringe.append(ins)
    # if gls != fringe[0]:
    #     n = neighbour_expand(fringe[0])
    #     for i in range(len(n)):
    #         if n[i] is not None:
    #             fringe.append(n[i])
    #         else:
    #             continue
    #     print(fringe[0])
    #     c = fringe.pop(0)
    #     c = tuple(map(tuple, c))
    #     closed.add(c)
    #     bfs(fringe[0], gls)
    #
    # else:
    #     print("Solution found")


# def dfs(ins, gls):
#     fringe.append(ins)
#     while fringe is not []:
#         if gls != fringe[-1]:
#             n = neighbour_expand(fringe[-1])
#             for i in n:
#                 if i is not None:
#                     fringe.append(i)
#                 else:
#                     continue
#             c = fringe.pop(-1)
#             c = tuple(map(tuple, c))
#             closed.add(c)
#             print("fringe")
#             print(fringe)
#             print("closed")
#             print(closed)
#         else:
#             print("Solution found")





# def ucs(ins, gls):
#     fringe.append(ins)
#     while fringe is not []:
#         if gls != fringe[0]:
#             n, cost = neighbour_expand(fringe[0])
#             for co, j in cost, n:
#                 dict = {
#                     co : j
#                 }
#     print(dict)


bfs(fringe, goal_state)
#dfs(fringe, goal_state)
#ucs(fringe, goal_state)


