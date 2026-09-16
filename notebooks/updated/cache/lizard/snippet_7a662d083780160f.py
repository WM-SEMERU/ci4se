def generate_random_ising_problem(solver, h_range=None, j_range=None):
    if h_range is None:
        h_range = solver.properties.get('h_range', [-1, 1])
    if j_range is None:
        j_range = solver.properties.get('j_range', [-1, 1])
    lin = {qubit: random.uniform(*h_range) for qubit in solver.nodes}
    quad = {edge: random.uniform(*j_range) for edge in solver.undirected_edges}
    return lin, quad