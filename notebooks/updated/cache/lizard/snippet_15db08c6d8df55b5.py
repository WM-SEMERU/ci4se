def merge_vertices(self):
    sorted_vertices = sorted(list(self.vertices.items()), key=lambda v:
        hash(v[1]))
    groups = []
    for k, g in groupby(sorted_vertices, lambda v: hash(v[1])):
        groups.append(list(g))
    for group in groups:
        if len(group) == 1:
            continue
        names = [v[0] for v in group]
        self.reduce_vertex(*names)