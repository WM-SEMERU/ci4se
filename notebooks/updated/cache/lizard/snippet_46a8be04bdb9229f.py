def trifurcate_base(cls, newick):
    t = cls(newick)
    t._tree.deroot()
    return t.newick