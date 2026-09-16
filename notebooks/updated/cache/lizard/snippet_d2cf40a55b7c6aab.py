def get_equivalent_kpoints(self, index):
    if self.kpoints[index].label is None:
        return [index]
    list_index_kpoints = []
    for i in range(len(self.kpoints)):
        if self.kpoints[i].label == self.kpoints[index].label:
            list_index_kpoints.append(i)
    return list_index_kpoints