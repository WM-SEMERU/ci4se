def match_tracks(self, set_a, set_b, closest_matches=False):
    costs = self.track_cost_matrix(set_a, set_b) * 100
    min_row_costs = costs.min(axis=1)
    min_col_costs = costs.min(axis=0)
    good_rows = np.where(min_row_costs < 100)[0]
    good_cols = np.where(min_col_costs < 100)[0]
    assignments = []
    if len(good_rows) > 0 and len(good_cols) > 0:
        if closest_matches:
            b_matches = costs[np.meshgrid(good_rows, good_cols, indexing='ij')
                ].argmin(axis=1)
            a_matches = np.arange(b_matches.size)
            initial_assignments = [(good_rows[a_matches[x]], good_cols[
                b_matches[x]]) for x in range(b_matches.size)]
        else:
            munk = Munkres()
            initial_assignments = munk.compute(costs[np.meshgrid(good_rows,
                good_cols, indexing='ij')].tolist())
            initial_assignments = [(good_rows[x[0]], good_cols[x[1]]) for x in
                initial_assignments]
        for a in initial_assignments:
            if costs[a[0], a[1]] < 100:
                assignments.append(a)
    return assignments