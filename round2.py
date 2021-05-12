from networkx import *
import matplotlib.pyplot as plt
import math
import itertools
from queue import Queue
import numpy as np
import numpy.random
import pylab
import random

g = read_edgelist("dataset1.txt",
                  create_using=nx.Graph(), nodetype=int)

print('\n----------------------------------------------------------------------------------------------------------------------\n')
print('GIANT COMPONENT\n')
n_g = 0
for component in nx.connected_components(g):
    n_g = max(n_g, len(component))
print('Size of the giant component - ' + str(n_g))


print('\n----------------------------------------------------------------------------------------------------------------------\n')
print('COMMUNITY DETECTION USING GIRVAN-NEWMAN\n')
tmp = 1
comp = networkx.algorithms.community.centrality.girvan_newman(g)
for communities in itertools.islice(comp, 5):
    print("Iteration # " + str(tmp))
    print(tuple(sorted(c) for c in communities))
    print()
    tmp += 1


print('\n----------------------------------------------------------------------------------------------------------------------\n')
print('CREATING BARABASI ALBERT MODEL\n')
g = barabasi_albert_graph(100, 25)

print('\n----------------------------------------------------------------------------------------------------------------------\n')
print('ASSIGNING ACTIVATION PROBABILITIES\n')
set_edge_attributes(g, values=0, name='weight')
arr = [[False] * 100 for i in range(100)]
vis = set()
q = Queue()
vis.add(0)
q.put(0)

while not q.empty():
    u = q.get()

    vis.add(u)
    x = 1
    f = 0

    for v in g.neighbors(u):
        if v not in vis:
            vis.add(v)
            q.put(v)

        if arr[u][v] is True or arr[v][u] is True:
            x -= g[u][v]['weight']
        else:
            f += 1

    k = 0
    lst = np.random.dirichlet(np.ones(f), size=1).tolist()[0]

    for v in g.neighbors(u):
        if arr[u][v] is False or arr[v][u] is False:
            arr[u][v] = arr[v][u] = True
            g[u][v]['weight'] = lst[k] * max(x, 0)
            k += 1


print('\n----------------------------------------------------------------------------------------------------------------------\n')
print('RUNNING ICM ALGORITHM\n')
for itr in range(0, 5):
    r = random.randint(0, 99)
    vis = set()
    q = Queue()
    q.put(r)
    activated = set()
    activated.add(r)
    steps = 0
    print("Initial set - " + str(activated))

    while not q.empty():
        steps += 1
        u = q.get()

        for v in g.neighbors(u):
            if v not in activated:
                rand = random.uniform(0, 0.5)
                if rand < g[u][v]['weight']:
                    q.put(v)
                    activated.add(v)

    print("Steps - " + str(steps))
    print()

print('\n----------------------------------------------------------------------------------------------------------------------\n')
