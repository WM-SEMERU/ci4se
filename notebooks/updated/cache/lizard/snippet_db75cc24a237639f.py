def genes_with_a_representative_sequence(self):
    return DictList(x for x in self.genes if x.protein.representative_sequence)