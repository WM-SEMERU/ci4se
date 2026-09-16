def prepare_calc_dir(self):
    with open('vasprun.conf', 'w') as f:
        f.write('NODES="nodes=%s:ppn=%d"\n' % (self.nodes, self.ppn))
        f.write('BLOCK=%d\n' % (self.block,))
        if self.ncl:
            f.write('NCL=%d\n' % (1,))