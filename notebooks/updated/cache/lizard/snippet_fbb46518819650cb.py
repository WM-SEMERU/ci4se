def _get_attrs(self):
    attrs = []
    attrs.append(('N Blocks', self.n_blocks, '{}'))
    bds = self.bounds
    attrs.append(('X Bounds', (bds[0], bds[1]), '{:.3f}, {:.3f}'))
    attrs.append(('Y Bounds', (bds[2], bds[3]), '{:.3f}, {:.3f}'))
    attrs.append(('Z Bounds', (bds[4], bds[5]), '{:.3f}, {:.3f}'))
    return attrs