def getCycleData(self, attri, fname, numtype='cycNum'):
    fname = self.findFile(fname, numtype)
    if self.inputdir == '':
        self.inputdir = self.sldir
    os.chdir(self.inputdir)
    self.sldir = os.getcwd() + '/'
    f = open(fname, 'r')
    lines = f.readlines()
    if self.inputdir != './':
        os.chdir(self.startdir)
        self.sldir = self.inputdir
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    for i in range(len(lines)):
        if lines[i].startswith('#'):
            lines[i] = lines[i].strip('#')
            tmp = lines[i].split()
            tmp1 = []
            for j in range(len(tmp)):
                if tmp[j] != '=' or '':
                    tmp1.append(tmp[j])
            tmp = tmp1
            for j in range(len(tmp)):
                if tmp[j] == attri:
                    try:
                        if '.' in tmp[j + 1]:
                            return float(tmp[j + 1])
                        else:
                            return int(tmp[j + 1])
                    except ValueError:
                        return str(tmp[j + 1])
        elif lines[i].startswith('H'):
            continue
        else:
            print('This cycle attribute does not exist')
            print('Returning None')
            return None