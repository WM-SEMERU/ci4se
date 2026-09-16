def _filter_utr(self, ex):
    coding_start = int(self.bed_tuple.thickStart)
    coding_end = int(self.bed_tuple.thickEnd)
    if coding_end - coding_start < 3:
        logger.debug(
            '{0} has an invalid coding region specified by thickStart and thickEnd (only {1} bps long). This gene is possibly either a non-coding transcript or a pseudo gene.'
            .format(self.gene_name, coding_end - coding_start))
        return []
    filtered_exons = []
    for exon in ex:
        if exon[0] > coding_end and exon[1] > coding_end:
            pass
        elif exon[0] < coding_start and exon[1] < coding_start:
            pass
        elif exon[0] <= coding_start and exon[1] >= coding_end:
            filtered_exons.append((coding_start, coding_end))
        elif exon[0] <= coding_start and exon[1] < coding_end:
            filtered_exons.append((coding_start, exon[1]))
        elif exon[0] > coding_start and exon[1] >= coding_end:
            filtered_exons.append((exon[0], coding_end))
        elif exon[0] > coding_start and exon[1] < coding_end:
            filtered_exons.append(exon)
        else:
            pass
    return filtered_exons