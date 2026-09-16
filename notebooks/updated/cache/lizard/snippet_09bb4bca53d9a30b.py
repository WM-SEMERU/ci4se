def get_edges(self):
    edge_from_to = []
    for parent, children in self.p_from_cs.items():
        for child in children:
            edge_from_to.append((child, parent))
    for parent, children in self.c_from_ps.items():
        for child in children:
            edge_from_to.append((child, parent))
    return edge_from_to