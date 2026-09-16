def estCumPos(pos, chrom, offset=20000000):
    chromvals = SP.unique(chrom)
    chrom_pos = SP.zeros_like(chromvals)
    cum_pos = SP.zeros_like(pos)
    maxpos_cum = 0
    for i, mychrom in enumerate(chromvals):
        chrom_pos[i] = maxpos_cum
        i_chr = chrom == mychrom
        maxpos = pos[i_chr].max() + offset
        maxpos_cum += maxpos
        cum_pos[i_chr] = chrom_pos[i] + pos[i_chr]
    return cum_pos, chrom_pos