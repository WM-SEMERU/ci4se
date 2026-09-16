def to_edgelist(self):
    export = []
    for edge in nx.to_edgelist(self.transforms):
        a, b, c = edge
        if 'geometry' in self.transforms.node[b]:
            c['geometry'] = self.transforms.node[b]['geometry']
        c['matrix'] = np.asanyarray(c['matrix'], dtype=np.float64).tolist()
        export.append((a, b, c))
    return export