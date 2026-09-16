def all_axis_bin_centers(self, axis):
    axis = self.get_axis_number(axis)
    return np.meshgrid(*self.bin_centers(), indexing='ij')[axis]