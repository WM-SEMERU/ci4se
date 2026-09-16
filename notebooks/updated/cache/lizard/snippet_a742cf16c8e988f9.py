def get_occurrence(self, occ):
    return self.lookup.pop((occ.event, occ.original_start, occ.original_end
        ), occ)