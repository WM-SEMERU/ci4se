def _estimate_paired_innerdist(fastq_file, pair_file, ref_file, out_base,
    out_dir, data):
    mean, stdev = _bowtie_for_innerdist('100000', fastq_file, pair_file,
        ref_file, out_base, out_dir, data, True)
    if not mean or not stdev:
        mean, stdev = _bowtie_for_innerdist('1', fastq_file, pair_file,
            ref_file, out_base, out_dir, data, True)
    if not mean or not stdev:
        mean, stdev = 200, 50
    return mean, stdev