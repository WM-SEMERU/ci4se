def get_stats(self):
    ostr = ''
    errtotal = self.deletions['total'] + self.insertions['total'
        ] + self.mismatches
    ostr += 'ALIGNMENT_COUNT\t' + str(self.alignment_count) + '\n'
    ostr += 'ALIGNMENT_BASES\t' + str(self.alignment_length) + '\n'
    ostr += 'ANY_ERROR\t' + str(errtotal) + '\n'
    ostr += 'MISMATCHES\t' + str(self.mismatches) + '\n'
    ostr += 'ANY_DELETION\t' + str(self.deletions['total']) + '\n'
    ostr += 'COMPLETE_DELETION\t' + str(self.deletions['specific']) + '\n'
    ostr += 'HOMOPOLYMER_DELETION\t' + str(self.deletions['homopolymer']
        ) + '\n'
    ostr += 'ANY_INSERTION\t' + str(self.insertions['total']) + '\n'
    ostr += 'COMPLETE_INSERTION\t' + str(self.insertions['specific']) + '\n'
    ostr += 'HOMOPOLYMER_INSERTION\t' + str(self.insertions['homopolymer']
        ) + '\n'
    return ostr