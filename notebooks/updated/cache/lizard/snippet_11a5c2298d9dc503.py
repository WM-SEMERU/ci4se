def radius_of_gyration(neurite):
    centre_mass = neurite_centre_of_mass(neurite)
    sum_sqr_distance = 0
    N = 0
    dist_sqr = [distance_sqr(centre_mass, s) for s in nm.iter_segments(neurite)
        ]
    sum_sqr_distance = np.sum(dist_sqr)
    N = len(dist_sqr)
    return np.sqrt(sum_sqr_distance / N)