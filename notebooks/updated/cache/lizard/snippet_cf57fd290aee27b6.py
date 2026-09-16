def smooth_data(self, data, config, is_3d=False):
    max_dist = config['Length_Limit'] * config['BandWidth']
    smoothed_value = np.zeros(len(data), dtype=float)
    for iloc in range(0, len(data)):
        dist_val = haversine(data[:, (0)], data[:, (1)], data[iloc, 0],
            data[iloc, 1])
        if is_3d:
            dist_val = np.sqrt(dist_val.flatten() ** 2.0 + (data[:, (2)] -
                data[iloc, 2]) ** 2.0)
        id0 = np.where(dist_val <= max_dist)[0]
        w_val = np.exp(-dist_val[id0] ** 2.0 / config['BandWidth'] ** 2.0
            ).flatten()
        smoothed_value[iloc] = np.sum(w_val * data[id0, 3]) / np.sum(w_val)
    return smoothed_value, np.sum(data[:, (-1)]), np.sum(smoothed_value)