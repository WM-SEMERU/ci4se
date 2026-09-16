def psnr(data, ground_truth, use_zscore=False, force_lower_is_better=False):
    if use_zscore:
        data = odl.util.zscore(data)
        ground_truth = odl.util.zscore(ground_truth)
    mse = mean_squared_error(data, ground_truth)
    max_true = np.max(np.abs(ground_truth))
    if mse == 0:
        result = np.inf
    elif max_true == 0:
        result = -np.inf
    else:
        result = 20 * np.log10(max_true) - 10 * np.log10(mse)
    if force_lower_is_better:
        return -result
    else:
        return result