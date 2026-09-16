def output_all_points(self):
    mass1 = []
    mass2 = []
    spin1z = []
    spin2z = []
    for i in self.massbank.keys():
        for j in self.massbank[i].keys():
            for k in xrange(len(self.massbank[i][j]['mass1s'])):
                curr_bank = self.massbank[i][j]
                mass1.append(curr_bank['mass1s'][k])
                mass2.append(curr_bank['mass2s'][k])
                spin1z.append(curr_bank['spin1s'][k])
                spin2z.append(curr_bank['spin2s'][k])
    return mass1, mass2, spin1z, spin2z