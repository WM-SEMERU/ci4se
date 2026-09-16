def _save_potentials(self, directory):
    print('saving potentials')
    digits = int(np.ceil(np.log10(self.configs.configs.shape[0])))
    for i in range(0, self.configs.configs.shape[0]):
        pot_data = self.get_potential(i)
        filename_raw = 'pot{0:0' + '{0}'.format(digits) + '}.dat'
        filename = directory + os.sep + filename_raw.format(i + 1)
        nodes = self.grid.nodes['sorted'][:, 1:3]
        all_data = np.hstack((nodes, pot_data[0][:, (np.newaxis)], pot_data
            [1][:, (np.newaxis)]))
        with open(filename, 'wb') as fid:
            np.savetxt(fid, all_data)