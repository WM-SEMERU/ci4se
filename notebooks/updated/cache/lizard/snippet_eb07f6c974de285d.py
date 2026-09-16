def sample(self):
    sample = []
    iterator = iter(self.__sample_extended_rows)
    iterator = self.__apply_processors(iterator)
    for row_number, headers, row in iterator:
        sample.append(row)
    return sample