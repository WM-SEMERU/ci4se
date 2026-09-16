def cleanup(self):
    if not len(self.water_ids) == 0:
        water_selection = []
        for wid in self.water_ids:
            water_selection.append('serialNumber=%i' % wid)
        self.rc('~display :HOH')
        self.rc('display :@/%s' % ' or '.join(water_selection))
    self.rc('~display #%i & ~:/isHet' % self.model_dict[self.plipname])
    self.rc('display :%s' % ','.join([str(self.atoms[bsid].residue.id) for
        bsid in self.bs_res_ids]))
    self.rc('color lightblue :HOH')