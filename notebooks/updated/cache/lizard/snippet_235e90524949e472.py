def json2lte(self, filename):
    data_json = open(filename, 'r').read().strip()
    latins = lattice.Lattice(data_json)
    self.lattice_instance = latins
    self.all_beamlines = latins.getAllBl()
    if self.use_beamline is None:
        self.use_beamline = ('BL' if 'BL' in self.all_beamlines else self.
            all_beamlines[0])
    bl_ele_list = [latins.getFullBeamline(k, True) for k in self.all_beamlines]
    self.beamlines_dict = dict(zip(self.all_beamlines, bl_ele_list))
    data_lte = latins.generateLatticeFile(self.use_beamline, 'sio')
    return data_json, data_lte