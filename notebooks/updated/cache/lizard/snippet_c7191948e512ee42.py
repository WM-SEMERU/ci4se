def get_column(self, chrom, position, missing_seqs=MissingSequenceHandler.
    TREAT_AS_ALL_GAPS, species=None):
    blocks = self.get_blocks(chrom, position, position + 1)
    if len(blocks) == 0:
        raise NoSuchAlignmentColumnError('Request for column on chrom ' +
            chrom + ' at position ' + str(position) + ' not possible; ' +
            'genome alignment not defined at ' + 'that locus.')
    if len(blocks) > 1:
        raise NoUniqueColumnError('Request for column on chrom ' + chrom +
            ' at position ' + str(position) + 'not ' +
            'possible; ambiguous alignment of that locus.')
    return blocks[0].get_column_absolute(position, missing_seqs, species)