def estimate_fragment_size(bam_file, nreads=5000):
    with open_samfile(bam_file) as bam_handle:
        reads = tz.itertoolz.take(nreads, bam_handle)
        lengths = [x.template_length for x in reads if x.template_length > 0]
    if not lengths:
        return 0
    return int(numpy.median(lengths))