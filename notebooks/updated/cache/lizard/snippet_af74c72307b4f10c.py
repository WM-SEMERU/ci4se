def make_SimData(g):
    return SimData([i.position for i in g.mutations()], [i for i in g.
        haplotypes()])