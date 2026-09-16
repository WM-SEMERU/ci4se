def get_depth_per_transcript(self, mindepth=1):
    bedarray = []
    for tx in self.get_transcripts():
        for ex in [x.range for x in tx.exons]:
            bedarray.append(ex)
    cov = ranges_to_coverage(bedarray)
    results = {}
    for tx in self.get_transcripts():
        tlen = tx.length
        bcov = []
        for ex in [x.range for x in tx.exons]:
            excov = [[x.overlap_size(ex), x.payload] for x in cov]
            for coved in [x for x in excov if x[0] > 0]:
                bcov.append(coved)
        total_base_coverage = sum([(x[0] * x[1]) for x in bcov])
        average_coverage = float(total_base_coverage) / float(tlen)
        minimum_bases_covered = sum([x[0] for x in bcov if x[1] >= mindepth])
        fraction_covered_at_minimum = float(minimum_bases_covered) / float(tlen
            )
        res = {'tx': tx, 'average_coverage': average_coverage,
            'fraction_covered': fraction_covered_at_minimum, 'mindepth':
            mindepth, 'length_covered': minimum_bases_covered}
        results[tx.id] = res
    return results