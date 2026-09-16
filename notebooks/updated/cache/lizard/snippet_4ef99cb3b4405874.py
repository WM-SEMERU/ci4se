def write_mesa(self, mesa_isos_file='isos.txt', add_excess_iso='fe56',
    outfile='xa_iniabu.dat', header_string=
    'initial abundances for a MESA run', header_char='!'):
    f = open('isos.txt')
    a = f.readlines()
    isos = []
    for i in range(len(a)):
        isos.append(a[i].strip().rstrip(','))
    mesa_names = []
    abus = []
    for i in range(len(self.z)):
        b = self.names[i].split()
        a = ''
        a = a.join(b)
        if a in isos:
            mesa_names.append(a)
            abus.append(self.abu[i])
    for i in range(len(isos)):
        if isos[i] not in mesa_names:
            mesa_names.append(isos[i])
            abus.append(0.0)
    excess = 1.0 - np.sum(np.array(abus))
    abus = np.array(abus)
    abus[mesa_names.index(add_excess_iso)] += excess
    dcols = ['', '']
    data = [mesa_names, abus]
    hd = [header_string]
    att.write(outfile, hd, dcols, data, header_char=header_char)
    return mesa_names, abus