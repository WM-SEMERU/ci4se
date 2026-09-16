def random_host_extinction(log, sampleNumber, extinctionType,
    extinctionConstant, hostExtinctionDistributions, plot=False):
    import numpy as np
    if extinctionType == 'constant':
        hostExtinctionArray = np.zeros(sampleNumber) * extinctionConstant
    else:
        log.error('host extiction distributions not included yet')
    return hostExtinctionArray