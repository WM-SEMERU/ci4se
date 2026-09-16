def _linear_selection(self, non_empty_slices, num_slices):
    num_non_empty = len(non_empty_slices)
    sampled_indices = np.linspace(0, num_non_empty, num=min(num_non_empty,
        num_slices), endpoint=False)
    slices_in_dim = non_empty_slices[np.around(sampled_indices).astype('int64')
        ]
    return slices_in_dim