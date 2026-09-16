def merge_down_loci(self):
    old_locus_size = -1
    z = 0
    while len(self.loci) != old_locus_size:
        z += 1
        old_locus_size = len(self.loci)
        locus_size = len(self.loci)
        if self.verbose:
            sys.stderr.write(str(locus_size) + ' Combining down loci step ' +
                str(z) + '       \r')
        combined = set()
        for i in range(0, locus_size):
            if i in combined:
                continue
            for j in range(i + 1, locus_size):
                if self.loci[i].range.overlaps_with_padding(self.loci[j].
                    range, self.overhang):
                    if self.use_direction and self.loci[i
                        ].range.direction != self.loci[j].range.direction:
                        continue
                    for obj in self.loci[j].members:
                        self.loci[i].add_member(obj)
                    combined.add(j)
                    break
        newloci = []
        for i in range(0, locus_size):
            if i not in combined:
                newloci.append(self.loci[i])
        self.loci = newloci
    if self.verbose:
        sys.stderr.write('Finished combining down ' + str(len(self.loci)) +
            ' loci in ' + str(z) + ' steps   \n')
    return