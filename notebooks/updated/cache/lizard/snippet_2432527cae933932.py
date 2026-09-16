def isotopic_variants(composition, npeaks=None, charge=0, charge_carrier=PROTON
    ):
    if npeaks is None:
        max_n_variants = max_variants(composition)
        npeaks = int(sqrt(max_n_variants) - 2)
        npeaks = max(npeaks, 3)
    else:
        npeaks -= 1
    return IsotopicDistribution(composition, npeaks
        ).aggregated_isotopic_variants(charge, charge_carrier=charge_carrier)