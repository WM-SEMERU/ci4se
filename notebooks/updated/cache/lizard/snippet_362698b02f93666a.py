def get_average_along_axis(self, ind):
    m = self.data['total']
    ng = self.dim
    if ind == 0:
        total = np.sum(np.sum(m, axis=1), 1)
    elif ind == 1:
        total = np.sum(np.sum(m, axis=0), 1)
    else:
        total = np.sum(np.sum(m, axis=0), 0)
    return total / ng[(ind + 1) % 3] / ng[(ind + 2) % 3]