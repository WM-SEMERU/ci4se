def add_data_individual(self, data_curie, label=None, ind_type=None):
    part_length = len(data_curie.split(':'))
    if part_length == 0:
        curie = '_:{}'.format(data_curie)
    elif part_length > 2:
        raise ValueError('Misformatted curie {}'.format(data_curie))
    else:
        curie = data_curie
    self.model.addIndividualToGraph(curie, label, ind_type)
    return