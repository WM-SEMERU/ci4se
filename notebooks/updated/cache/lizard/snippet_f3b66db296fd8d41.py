def conservtion_profile_pid(region, genome_alignment, mi_seqs=
    MissingSequenceHandler.TREAT_AS_ALL_GAPS, species=None):
    res = []
    s = region.start if region.isPositiveStrand() else region.end - 1
    e = region.end if region.isPositiveStrand() else region.start - 1
    step = 1 if region.isPositiveStrand() else -1
    for i in range(s, e, step):
        try:
            col = genome_alignment.get_column(region.chrom, i, mi_seqs, species
                )
            res.append(pid(col))
        except NoSuchAlignmentColumnError:
            res.append(None)
        except NoUniqueColumnError:
            res.append(None)
    return res