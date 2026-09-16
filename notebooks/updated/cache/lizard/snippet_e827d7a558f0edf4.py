def tot_edges(self):
    all_edges = []
    for facet in self.facets:
        edges = []
        pt = self.get_line_in_facet(facet)
        lines = []
        for i, p in enumerate(pt):
            if i == len(pt) / 2:
                break
            lines.append(tuple(sorted(tuple([tuple(pt[i * 2]), tuple(pt[i *
                2 + 1])]))))
        for i, p in enumerate(lines):
            if p not in all_edges:
                edges.append(p)
        all_edges.extend(edges)
    return len(all_edges)