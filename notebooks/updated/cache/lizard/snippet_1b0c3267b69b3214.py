def filter(fastq, sam, paired=False):
    if paired is False:
        list = sam_list(sam)
    else:
        list = sam_list_paired(sam)
    if paired is False:
        filter_fastq(fastq, list)
    else:
        filter_fastq_paired(fastq, list)