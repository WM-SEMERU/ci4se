def pairwise_indices(self, alpha=0.05, only_larger=True, hs_dims=None):
    return PairwiseSignificance(self, alpha=alpha, only_larger=only_larger,
        hs_dims=hs_dims).pairwise_indices