def isoratio_init(self, isos):
    if len(isos) == 2:
        dumb = []
        dumb = isos[0].split('-')
        dumb.append(isos[1].split('-')[0])
        dumb.append(isos[1].split('-')[1])
        isos = dumb
    ssratio = old_div(self.habu[isos[0].ljust(2).lower() + str(int(isos[1])
        ).rjust(3)], self.habu[isos[2].ljust(2).lower() + str(int(isos[3]))
        .rjust(3)])
    return ssratio