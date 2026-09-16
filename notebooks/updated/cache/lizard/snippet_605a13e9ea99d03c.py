def sum(self, vector):
    return self.from_list([(x + vector.vector[i]) for i, x in self.to_list()])