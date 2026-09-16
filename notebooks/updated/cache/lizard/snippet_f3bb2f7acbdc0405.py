def open_pysam_file(fname, ftype):
    try:
        if ftype == 'bam':
            fpysam = pysam.AlignmentFile(fname, 'rb')
        elif ftype == 'fasta':
            fpysam = pysam.FastaFile(fname)
        yield fpysam
    except:
        raise
    else:
        fpysam.close()