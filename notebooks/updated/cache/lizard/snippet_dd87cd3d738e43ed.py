def genes_with_experimental_structures(self):
    return DictList(x for x in self.genes_with_structures if x.protein.
        num_structures_experimental > 0)