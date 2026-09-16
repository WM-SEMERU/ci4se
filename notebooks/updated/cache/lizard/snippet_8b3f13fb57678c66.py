def prt_ev_cnts(self, ctr, prt=sys.stdout):
    for key, cnt in ctr.most_common():
        grp, name = self.get_grp_name(key.replace('NOT ', ''))
        prt.write('{CNT:7,} {EV:>7} {GROUP:<15} {NAME}\n'.format(CNT=cnt,
            EV=key, GROUP=grp, NAME=name))