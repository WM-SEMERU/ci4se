def genome_alignment_iterator(fn, reference_species, index_friendly=False,
    verbose=False):
    kw_args = {'reference_species': reference_species}
    for e in maf.maf_iterator(fn, index_friendly=index_friendly,
        yield_class=GenomeAlignmentBlock, yield_kw_args=kw_args, verbose=
        verbose):
        yield e