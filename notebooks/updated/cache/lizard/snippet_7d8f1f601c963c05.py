def _generate_noise_system(dimensions_tr, spatial_sd, temporal_sd,
    spatial_noise_type='gaussian', temporal_noise_type='gaussian'):

    def noise_volume(dimensions, noise_type):
        if noise_type == 'rician':
            noise = stats.rice.rvs(b=0, loc=0, scale=1.527, size=dimensions)
        elif noise_type == 'exponential':
            noise = stats.expon.rvs(0, scale=1, size=dimensions)
        elif noise_type == 'gaussian':
            noise = np.random.randn(np.prod(dimensions)).reshape(dimensions)
        return noise
    dimensions = np.asarray([dimensions_tr[0], dimensions_tr[1],
        dimensions_tr[2], 1])
    spatial_noise = noise_volume(dimensions, spatial_noise_type)
    temporal_noise = noise_volume(dimensions_tr, temporal_noise_type)
    spatial_noise *= spatial_sd
    temporal_noise *= temporal_sd
    temporal_noise_mean = np.mean(temporal_noise, 3).reshape(dimensions[0],
        dimensions[1], dimensions[2], 1)
    temporal_noise = temporal_noise - temporal_noise_mean
    system_noise = spatial_noise + temporal_noise
    return system_noise