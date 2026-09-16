def label_storm_objects(data, method, min_intensity, max_intensity,
    min_area=1, max_area=100, max_range=1, increment=1, gaussian_sd=0):
    if method.lower() in ['ew', 'watershed']:
        labeler = EnhancedWatershed(min_intensity, increment, max_intensity,
            max_area, max_range)
    else:
        labeler = Hysteresis(min_intensity, max_intensity)
    if len(data.shape) == 2:
        label_grid = labeler.label(gaussian_filter(data, gaussian_sd))
        label_grid[data < min_intensity] = 0
        if min_area > 1:
            label_grid = labeler.size_filter(label_grid, min_area)
    else:
        label_grid = np.zeros(data.shape, dtype=int)
        for t in range(data.shape[0]):
            label_grid[t] = labeler.label(gaussian_filter(data[t], gaussian_sd)
                )
            label_grid[t][data[t] < min_intensity] = 0
            if min_area > 1:
                label_grid[t] = labeler.size_filter(label_grid[t], min_area)
    return label_grid