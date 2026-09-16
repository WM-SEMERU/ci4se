def series_in_dir(self):
    countsd = {}
    for line in self.files_with_info:
        if 'SeriesNumber' in line:
            sn = line['SeriesNumber']
        else:
            sn = None
        if sn in countsd:
            countsd[sn] += 1
        else:
            countsd[sn] = 1
    bins = list(countsd)
    counts = list(countsd.values())
    return counts, bins