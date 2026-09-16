def is_preemptible(self):
    nodes = []
    for node in self.nodes:
        if Kurz.is_preemtible(node):
            nodes.append(node)
    return self