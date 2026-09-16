def add_star(self, nodes, t=None):
    nlist = list(nodes)
    v = nlist[0]
    interaction = ((v, n) for n in nlist[1:])
    self.add_interactions_from(interaction, t)