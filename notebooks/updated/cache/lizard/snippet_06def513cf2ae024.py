def land_threshold(self, land_cloud_prob, pcps, water):
    clearsky_land = ~(pcps | water)
    cloud_prob = land_cloud_prob.copy()
    cloud_prob[~clearsky_land] = np.nan
    cloud_prob[~self.mask] = np.nan
    th_const = 0.2
    return np.nanpercentile(cloud_prob, 82.5) + th_const