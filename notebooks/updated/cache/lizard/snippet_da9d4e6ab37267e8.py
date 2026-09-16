def sb_filter(fastq, bc, cores, nedit):
    barcodes = set(sb.strip() for sb in bc)
    if nedit == 0:
        filter_sb = partial(exact_sample_filter2, barcodes=barcodes)
    else:
        barcodehash = MutationHash(barcodes, nedit)
        filter_sb = partial(correcting_sample_filter2, barcodehash=barcodehash)
    p = multiprocessing.Pool(cores)
    chunks = tz.partition_all(10000, read_fastq(fastq))
    bigchunks = tz.partition_all(cores, chunks)
    for bigchunk in bigchunks:
        for chunk in p.map(filter_sb, list(bigchunk)):
            for read in chunk:
                sys.stdout.write(read)