def load(self, filename):
    assert os.path.exists(filename), "couldn't find control file {0}".format(
        filename)
    f = open(filename, 'r')
    while True:
        line = f.readline()
        if line == '':
            raise Exception(
                'Pst.load() error: EOF when trying to find first line - #sad')
        if line.strip().split()[0].lower() == 'pcf':
            break
    assert line.startswith('pcf'
        ), "Pst.load() error: first noncomment line must start with 'pcf', not '{0}'".format(
        line)
    raw = line.strip().split()
    if len(raw) > 1 and 'version' in raw[1].lower():
        raw = raw[1].split('=')
        if len(raw) > 1:
            try:
                self._version = int(raw[1])
            except:
                pass
    if self._version == 1:
        self._load_version1(filename)
    elif self._version == 2:
        self._load_version2(filename)
    else:
        raise Exception("Pst.load() error: version must be 1 or 2, not '{0}'"
            .format(version))