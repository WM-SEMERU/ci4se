def fromvcf(filename, chrom=None, start=None, stop=None, samples=True):
    return VCFView(filename, chrom=chrom, start=start, stop=stop, samples=
        samples)