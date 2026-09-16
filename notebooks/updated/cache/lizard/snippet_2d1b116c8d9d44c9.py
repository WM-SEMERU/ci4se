def view(self, vleaf, fpath=None, cleanup=True, format=None):
    graph = self.create_graphviz_digraph(vleaf, format=format)
    graph.view(fpath, cleanup=cleanup)