def display_start(self):
    if self.opt['Verbose']:
        if self.opt['AutoRho', 'Enabled']:
            hdrtxt = type(self).hdrtxt()
        else:
            hdrtxt = type(self).hdrtxt()[0:-1]
        hdrstr, fmtstr, nsep = common.solve_status_str(hdrtxt, fwdth0=type(
            self).fwiter, fprec=type(self).fpothr)
        if self.opt['StatusHeader']:
            print(hdrstr)
            print('-' * nsep)
    else:
        fmtstr, nsep = '', 0
    return fmtstr, nsep