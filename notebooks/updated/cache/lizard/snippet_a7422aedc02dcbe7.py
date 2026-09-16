def file_plus_index(fname):
    exts = {'.vcf': '.idx', '.bam': '.bai', '.vcf.gz': '.tbi', '.bed.gz':
        '.tbi', '.fq.gz': '.gbi'}
    ext = splitext_plus(fname)[-1]
    if ext in exts:
        return [fname, fname + exts[ext]]
    else:
        return [fname]