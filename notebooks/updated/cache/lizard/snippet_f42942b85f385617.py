def _sim_WA(trace, PAZ, seedresp, water_level, velocity=False):
    PAZ_WA = {'poles': [-6.283 + 4.7124j, -6.283 - 4.7124j], 'zeros': [0 + 
        0.0j], 'gain': 1.0, 'sensitivity': 2080}
    if velocity:
        PAZ_WA['zeros'] = [0 + 0.0j, 0 + 0.0j]
    trace.detrend('simple')
    if PAZ:
        trace.data = seis_sim(trace.data, trace.stats.sampling_rate,
            paz_remove=PAZ, paz_simulate=PAZ_WA, water_level=water_level,
            remove_sensitivity=True)
    elif seedresp:
        trace.data = seis_sim(trace.data, trace.stats.sampling_rate,
            paz_remove=None, paz_simulate=PAZ_WA, water_level=water_level,
            seedresp=seedresp)
    else:
        UserWarning('No response given to remove, will just simulate WA')
        trace.data = seis_sim(trace.data, trace.stats.sampling_rate,
            paz_remove=None, paz_simulate=PAZ_WA, water_level=water_level)
    return trace