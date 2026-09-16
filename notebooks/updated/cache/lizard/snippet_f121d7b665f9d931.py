def parse_cigar(cigar):
    cigar = cigar.replace('M', 'M ').replace('I', 'I ').replace('D', 'D '
        ).split()
    cigar = [c.replace('M', ' M').replace('I', ' I').replace('D', ' D').
        split() for c in cigar]
    return [(int(c[0]), c[1]) for c in cigar]