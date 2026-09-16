def mask_right(self, n_seq_bases, mask='S'):
    return Cigar(Cigar(self._reverse_cigar()).mask_left(n_seq_bases, mask).
        _reverse_cigar())