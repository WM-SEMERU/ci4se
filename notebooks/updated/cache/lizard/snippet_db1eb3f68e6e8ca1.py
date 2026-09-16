def read_internal_strain_tensor(self):
    search = []

    def internal_strain_start(results, match):
        results.internal_strain_ion = int(match.group(1)) - 1
        results.internal_strain_tensor.append(np.zeros((3, 6)))
    search.append([
        'INTERNAL STRAIN TENSOR FOR ION\\s+(\\d+)\\s+for displacements in x,y,z  \\(eV/Angst\\):'
        , None, internal_strain_start])

    def internal_strain_data(results, match):
        if match.group(1).lower() == 'x':
            index = 0
        elif match.group(1).lower() == 'y':
            index = 1
        elif match.group(1).lower() == 'z':
            index = 2
        else:
            raise Exception(
                "Couldn't parse row index from symbol for internal strain tensor: {}"
                .format(match.group(1)))
        results.internal_strain_tensor[results.internal_strain_ion][index
            ] = np.array([float(match.group(i)) for i in range(2, 8)])
        if index == 2:
            results.internal_strain_ion = None
    search.append(['^\\s+([x,y,z])\\s+' + '([-]?\\d+\\.\\d+)\\s+' * 6, lambda
        results, line: results.internal_strain_ion is not None,
        internal_strain_data])
    self.internal_strain_ion = None
    self.internal_strain_tensor = []
    micro_pyawk(self.filename, search, self)