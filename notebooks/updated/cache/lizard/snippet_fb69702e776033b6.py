def _double_gamma_hrf(response_delay=6, undershoot_delay=12,
    response_dispersion=0.9, undershoot_dispersion=0.9, response_scale=1,
    undershoot_scale=0.035, temporal_resolution=100.0):
    hrf_length = 30
    hrf = [0] * int(hrf_length * temporal_resolution)
    response_peak = response_delay * response_dispersion
    undershoot_peak = undershoot_delay * undershoot_dispersion
    for hrf_counter in list(range(len(hrf) - 1)):
        resp_pow = math.pow(hrf_counter / temporal_resolution /
            response_peak, response_delay)
        resp_exp = math.exp(-(hrf_counter / temporal_resolution -
            response_peak) / response_dispersion)
        response_model = response_scale * resp_pow * resp_exp
        undershoot_pow = math.pow(hrf_counter / temporal_resolution /
            undershoot_peak, undershoot_delay)
        undershoot_exp = math.exp(-(hrf_counter / temporal_resolution - 
            undershoot_peak / undershoot_dispersion))
        undershoot_model = undershoot_scale * undershoot_pow * undershoot_exp
        hrf[hrf_counter] = response_model - undershoot_model
    return hrf