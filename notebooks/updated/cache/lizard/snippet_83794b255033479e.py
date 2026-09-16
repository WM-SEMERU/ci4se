def _tighten_triplet(self, max_iterations, later_iter, max_triplets, prolong):
    triangles = self.find_triangles()
    triplet_scores = self._get_triplet_scores(triangles)
    sorted_scores = sorted(triplet_scores, key=triplet_scores.get)
    for niter in range(max_iterations):
        if self._is_converged(integrality_gap_threshold=self.
            integrality_gap_threshold):
            break
        add_triplets = []
        for triplet_number in range(len(sorted_scores)):
            if triplet_number >= max_triplets:
                break
            add_triplets.append(sorted_scores.pop())
        if not add_triplets and prolong is False:
            break
        self._update_triangles(add_triplets)
        self._run_mplp(later_iter)