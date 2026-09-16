def name_match(self, wfn):
    for N in self.K:
        if CPESet2_3.cpe_superset(wfn, N):
            return True
    return False