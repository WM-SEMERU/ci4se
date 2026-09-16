def seqres_lines(self):
    lines = []
    for chain in self.keys():
        seq = self[chain]
        serNum = 1
        startidx = 0
        while startidx < len(seq):
            endidx = min(startidx + 13, len(seq))
            lines += ['SEQRES  %2i %s %4i  %s\n' % (serNum, chain, len(seq),
                ' '.join(seq[startidx:endidx]))]
            serNum += 1
            startidx += 13
    return lines