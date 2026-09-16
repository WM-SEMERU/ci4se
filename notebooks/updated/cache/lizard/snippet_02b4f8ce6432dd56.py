def _station_load(network, station, crit_stations):
    if isinstance(station, LVStation):
        grid_level = 'lv'
    else:
        grid_level = 'mv'
    s_station = sum([_.type.S_nom for _ in station.transformers])
    s_station_allowed_per_case = {}
    s_station_allowed_per_case['feedin_case'] = s_station * network.config[
        'grid_expansion_load_factors']['{}_feedin_case_transformer'.format(
        grid_level)]
    s_station_allowed_per_case['load_case'] = s_station * network.config[
        'grid_expansion_load_factors']['{}_load_case_transformer'.format(
        grid_level)]
    s_station_allowed = (network.timeseries.timesteps_load_feedin_case.case
        .apply(lambda _: s_station_allowed_per_case[_]))
    try:
        if isinstance(station, LVStation):
            s_station_pfa = network.results.s_res(station.transformers).sum(
                axis=1)
        else:
            s_station_pfa = network.results.s_res([station]).iloc[:, (0)]
        s_res = s_station_allowed - s_station_pfa
        s_res = s_res[s_res < 0]
        if not s_res.empty:
            load_factor = (network.timeseries.timesteps_load_feedin_case.
                case.apply(lambda _: network.config[
                'grid_expansion_load_factors']['{}_{}_transformer'.format(
                grid_level, _)]))
            relative_s_res = load_factor * s_res
            crit_stations = crit_stations.append(pd.DataFrame({'s_pfa':
                s_station_pfa.loc[relative_s_res.idxmin()], 'time_index':
                relative_s_res.idxmin()}, index=[station]))
    except KeyError:
        logger.debug('No results for {} station to check overloading.'.
            format(grid_level.upper()))
    return crit_stations