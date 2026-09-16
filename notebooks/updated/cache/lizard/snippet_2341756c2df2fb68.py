def get_events(self, rlzs_by_gsim):
    all_eids, rlzs = [], []
    for rlz, eids in self.get_eids_by_rlz(rlzs_by_gsim).items():
        all_eids.extend(eids)
        rlzs.extend([rlz] * len(eids))
    return numpy.fromiter(zip(all_eids, rlzs), events_dt)