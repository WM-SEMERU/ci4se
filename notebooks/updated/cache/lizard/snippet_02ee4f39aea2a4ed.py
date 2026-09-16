def _read_starlog(self):
    sldir = self.sldir
    slname = self.slname
    slaname = slname + 'sa'
    if not os.path.exists(sldir + '/' + slaname):
        print('No ' + self.slname + 'sa file found, create new one from ' +
            self.slname)
        _cleanstarlog(sldir + '/' + slname)
    elif self.clean_starlog:
        print('Requested new ' + self.slname + 'sa; create new from ' +
            self.slname)
        _cleanstarlog(sldir + '/' + slname)
    else:
        print('Using old ' + self.slname + 'sa file ...')
    cmd = os.popen('wc ' + sldir + '/' + slaname)
    cmd_out = cmd.readline()
    cnum_cycles = cmd_out.split()[0]
    num_cycles = int(cnum_cycles) - 6
    filename = sldir + '/' + slaname
    header_attr, cols, data = _read_mesafile(filename, data_rows=num_cycles)
    self.cols = cols
    self.header_attr = header_attr
    self.data = data