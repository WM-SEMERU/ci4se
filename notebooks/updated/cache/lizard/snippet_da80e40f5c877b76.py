def get_all_nn_info(self, structure):
    return [self.get_nn_info(structure, n) for n in range(len(structure))]