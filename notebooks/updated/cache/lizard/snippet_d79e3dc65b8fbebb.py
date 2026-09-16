def _check_targets_input(targets, data):
    if isinstance(targets, np.ndarray) or isinstance(targets, list):
        targets, n_TRs, n_voxels, n_subjects = _check_timeseries_input(targets)
        if data.shape[0] != n_TRs:
            raise ValueError(
                'Targets array must have same number of TRs as input data')
        if data.shape[2] != n_subjects:
            raise ValueError(
                'Targets array must have same number of subjects as input data'
                )
        symmetric = False
    else:
        targets = data
        n_TRs, n_voxels, n_subjects = data.shape
        symmetric = True
    return targets, n_TRs, n_voxels, n_subjects, symmetric