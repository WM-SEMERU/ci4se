def _beta(catchment):
    lnbeta = -1.1221 - 0.0816 * log(catchment.descriptors.dtm_area
        ) - 0.458 * log(catchment.descriptors.saar / 1000) + 0.1065 * log(
        catchment.descriptors.bfihost)
    return exp(lnbeta)