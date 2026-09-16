def restore(self, filename):
    matfile = loadmat(filename)
    if matfile['dim'] == 1:
        matfile['solution'] = matfile['solution'][(0), :]
    self.elapsed_time = matfile['elapsed_time'][0, 0]
    self.solution = matfile['solution']
    return self