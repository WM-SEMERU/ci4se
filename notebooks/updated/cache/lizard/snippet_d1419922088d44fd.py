def generate_covalent_bond_graph(covalent_bonds):
    bond_graph = networkx.Graph()
    for inter in covalent_bonds:
        bond_graph.add_edge(inter.a, inter.b)
    return bond_graph