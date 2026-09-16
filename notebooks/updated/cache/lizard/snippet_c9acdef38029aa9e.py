def get_grouped_indices(self, voigt=False, **kwargs):
    if voigt:
        array = self.voigt
    else:
        array = self
    indices = list(itertools.product(*[range(n) for n in array.shape]))
    remaining = indices.copy()
    grouped = [list(zip(*np.where(np.isclose(array, 0, **kwargs))))]
    remaining = [i for i in remaining if i not in grouped[0]]
    while remaining:
        new = list(zip(*np.where(np.isclose(array, array[remaining[0]], **
            kwargs))))
        grouped.append(new)
        remaining = [i for i in remaining if i not in new]
    return [g for g in grouped if g]