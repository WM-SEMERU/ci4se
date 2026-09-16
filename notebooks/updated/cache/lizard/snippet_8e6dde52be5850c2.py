def prt_txt(self, prt=sys.stdout, pre=''):
    data_nts = self.get_d1nts()
    for ntdata in data_nts:
        prt.write('{PRE}{L:1} {NS} {d:6,} D{D:02} {GO} {NAME}\n'.format(PRE
            =pre, L=ntdata.D1, d=ntdata.dcnt, NS=ntdata.NS, D=ntdata.depth,
            GO=ntdata.GO, NAME=ntdata.name))
    return data_nts