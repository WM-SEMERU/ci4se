def _read_potentials(self, pot_dir):
    if self.assignments['potentials'] is not None:
        print('Potentials already imported. Will not overwrite!')
        return
    else:
        self.assignments['potentials'] = {}
    pot_files = sorted(glob(pot_dir + os.sep + 'pot*.dat'))
    for nr, filename in enumerate(pot_files):
        with open(filename, 'r') as fid:
            pot_data = np.loadtxt(fid)
            nids = self.nodeman.add_data(pot_data[:, 2:4])
            self.assignments['potentials'][nr] = nids