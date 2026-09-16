def get_sequence(self, chrom, start, end, strand='+', indexing=(-1, 0)):
    try:
        divisor = int(self.sequence_index[chrom][2])
    except KeyError:
        self.open_fasta_index()
        try:
            divisor = int(self.sequence_index[chrom][2])
        except KeyError:
            sys.stderr.write(
                '%s cannot be found within the fasta index file.\n' % chrom)
            return ''
    start += indexing[0]
    end += indexing[1]
    if start < 0 or end > int(self.sequence_index[chrom][0]):
        raise ValueError(
            'The range %d-%d is invalid. Valid range for this feature is 1-%d.'
             % (start - indexing[0], end - indexing[1], int(self.
            sequence_index[chrom][0])))
    seekpos = int(self.sequence_index[chrom][1])
    seekpos += start + start / divisor
    slen = end - start
    endpos = int(slen + slen / divisor + 1)
    self.fasta_file.seek(seekpos, 0)
    output = self.fasta_file.read(endpos)
    output = output.replace('\n', '')
    out = output[:slen]
    if strand == '+' or strand == 1:
        return out
    if strand == '-' or strand == -1:
        return _reverse_complement(out)