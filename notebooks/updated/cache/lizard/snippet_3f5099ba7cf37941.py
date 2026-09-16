def _write_multiplicons(self, filename):
    mhead = '\t'.join(['id', 'genome_x', 'list_x', 'parent', 'genome_y',
        'list_y', 'level', 'number_of_anchorpoints', 'profile_length',
        'begin_x', 'end_x', 'begin_y', 'end_y', 'is_redundant'])
    with open(filename, 'w') as fhandle:
        fhandle.write(mhead + '\n')
        for mrow in self.multiplicons:
            fhandle.write('\t'.join([str(e) for e in mrow]) + '\n')