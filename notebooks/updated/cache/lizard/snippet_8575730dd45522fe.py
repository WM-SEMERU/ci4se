def all_characters(self):
    qs = self.assoc_characters.all()
    for node in self.get_descendants():
        qs2 = node.assoc_characters.all()
        qs = qs.union(qs2).distinct('pk')
    return qs