def make_vslc_label(self, gene_label, allele1_label, allele2_label):
    vslc_label = ''
    if gene_label is None and allele1_label is None and allele2_label is None:
        LOG.error('Not enough info to make vslc label')
        return None
    top = self.make_variant_locus_label(gene_label, allele1_label)
    bottom = ''
    if allele2_label is not None:
        bottom = self.make_variant_locus_label(gene_label, allele2_label)
    vslc_label = '/'.join((top, bottom))
    return vslc_label