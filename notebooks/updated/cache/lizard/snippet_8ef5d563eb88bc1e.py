def coverage_interval_from_bed(bed_file, per_chrom=True):
    total_starts = {}
    total_ends = {}
    bed_bases = collections.defaultdict(int)
    with utils.open_gzipsafe(bed_file) as in_handle:
        for line in in_handle:
            parts = line.split()
            if len(parts) >= 3:
                chrom, start, end = parts[:3]
                if chromhacks.is_autosomal(chrom):
                    start = int(start)
                    end = int(end)
                    bed_bases[chrom] += end - start
                    total_starts[chrom] = min([start, total_starts.get(
                        chrom, sys.maxsize)])
                    total_ends[chrom] = max([end, total_ends.get(chrom, 0)])
    if per_chrom:
        freqs = [(float(bed_bases[c]) / float(total_ends[c] - total_starts[
            c])) for c in sorted(bed_bases.keys())]
    elif len(bed_bases) > 0:
        freqs = [sum([bed_bases[c] for c in sorted(bed_bases.keys())]) /
            sum([float(total_ends[c] - total_starts[c]) for c in sorted(
            bed_bases.keys())])]
    else:
        freqs = []
    if any([(f >= 0.4) for f in freqs]):
        return 'genome'
    else:
        return 'targeted'