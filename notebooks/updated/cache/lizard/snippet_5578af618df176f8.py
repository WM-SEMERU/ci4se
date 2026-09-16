def volume(self):
    sizes = self.compute_cell_sizes(length=False, area=False, volume=True)
    return np.sum(sizes.cell_arrays['Volume'])