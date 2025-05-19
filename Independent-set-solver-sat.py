from pysat.formula import CNF
from pysat.card import CardEnc
from pysat.solvers import Minisat22
import math
import os
import time
import matplotlib.pyplot as plt

def read_graph(filepath ="graph.clq"): 
    # this function reads a graph from a file in the DIMACS format
    # The function returns a list of edges and the number of nodes in the graph
    edges = []
    num_nodes = 0

    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith('p edge'):
                parts = line.strip().split()
                num_nodes = int(parts[2])
            elif line.startswith('e'):
                _, u, v = line.strip().split()
                edges.append((int(u), int(v)))
    return edges, num_nodes

#print(read_graph("graph.clq"))
def build_independent_set_cnf(edges, num_nodes,k):
    # this function builds a CNF formula for the independent set problem    
    cnf = CNF()
    for u, v in edges:
        cnf.append([-u, -v])

    all_vars = list(range(1, num_nodes + 1))
    card = CardEnc.equals(lits=all_vars, bound=k, encoding=1)
    cnf.extend(card.clauses)

    return cnf

edges, num_nodes = read_graph("graph.clq")
#print (num_nodes)
#print (edges)
# cnf = build_independent_set_cnf(num_nodes,edges,k=5)
# cnf.to_file("output_k5.cnf")
def find_independent_set(cnf):
    # this function finds an independent set of size k in the graph
    # using the pysat library to solve the CNF formula
    start = time.time()
    with Minisat22(bootstrap_with=cnf) as solver:
        if solver.solve():
            model = solver.get_model()
            independent_set = [abs(x) for x in model if x > 0]
            end = time.time() - start
            return independent_set,end
        else:
            return None
def combinations(n, k):
    return math.comb(n, k)
# cnf = build_independent_set_cnf(edges, num_nodes, k=10)
# result = find_independent_set(cnf)
# if result:
#     print(f"Independent set found: {result[0]} and it took {result[1]} seconds")
# else:
#     print("No independent set found.")
solver_times = []
combinations_amount = []
k_numbs = list(range(3, 11))
for k in k_numbs: # this is the range of k values to test
    cnf = build_independent_set_cnf(edges, num_nodes, k=k)
    start = time.time()
    with Minisat22(bootstrap_with=cnf) as solver:
            doable = solver.solve()
    end = time.time() - start
    solver_times.append(end)
combinations_amount = [math.comb(num_nodes, k) for k in k_numbs]
def Interface(combinations_amount, solver_times,k_numbs):
    # this function plots the results of the solver times and combinations amount
    plt.figure(figsize=(10, 6))
    plt.plot(k_numbs, solver_times, marker='o', label='Solver Time(seconds)')
    plt.plot(k_numbs, combinations_amount, marker='x', label='Combinations Amount')
    plt.yscale('log')
    plt.xlabel('k')
    plt.ylabel('Time (seconds) / Combinations Amount')
    plt.title('Solver Time vs Combinations Amount')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()    
Interface(combinations_amount, solver_times,k_numbs) 
# using this method is much faster than using the brute force method then brute force method is not feasible for large graphs it would take a lot of time to find the independent set (almost impossible)