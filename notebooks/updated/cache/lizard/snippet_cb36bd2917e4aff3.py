def iter_variants(self):
    for idx, row in self.bim.iterrows():
        yield Variant(row.name, CHROM_INT_TO_STR[row.chrom], row.pos, [row.
            a1, row.a2])