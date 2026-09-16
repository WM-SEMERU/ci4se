def compute_search_volume_in_bins(found, total, ndbins, sim_to_bins_function):
    eff, err = compute_search_efficiency_in_bins(found, total, ndbins,
        sim_to_bins_function)
    dx = ndbins[0].upper() - ndbins[0].lower()
    r = ndbins[0].centres()
    vol = bin_utils.BinnedArray(bin_utils.NDBins(ndbins[1:]))
    errors = bin_utils.BinnedArray(bin_utils.NDBins(ndbins[1:]))
    vol.array = numpy.trapz(eff.array.T * 4.0 * numpy.pi * r ** 2, r, dx)
    errors.array = numpy.sqrt(((4 * numpy.pi * r ** 2 * err.array.T * dx) **
        2).sum(axis=-1))
    return vol, errors