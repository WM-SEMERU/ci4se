def _count_fastq_reads(in_fastq, min_reads):
    with open(in_fastq) as in_handle:
        items = list(itertools.takewhile(lambda i: i <= min_reads, (i for i,
            _ in enumerate(FastqGeneralIterator(in_handle)))))
    return len(items)