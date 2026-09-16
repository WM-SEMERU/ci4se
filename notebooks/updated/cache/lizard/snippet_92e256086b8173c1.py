def fill(self):
    self.frequency2umis = collections.defaultdict(list)
    for read in self.inbam:
        if read.is_unmapped:
            continue
        if read.is_read2:
            continue
        self.umis[self.barcode_getter(read)[0]] += 1
    self.umis_counter = collections.Counter(self.umis)
    total_umis = sum(self.umis_counter.values())
    U.info('total_umis %i' % total_umis)
    U.info('#umis %i' % len(self.umis_counter))
    self.prob = self.umis_counter.values()
    sum_prob = sum(self.prob)
    self.prob = [(float(x) / sum_prob) for x in self.prob]
    self.refill_random()