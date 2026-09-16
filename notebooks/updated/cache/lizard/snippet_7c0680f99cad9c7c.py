def _get_dfs(csvs):
    logger_dataframes.info('enter get_lipd_cols')
    dfs = {'chronData': {}, 'paleoData': {}}
    try:
        for filename, cols in csvs.items():
            tmp = {}
            for var, data in cols.items():
                tmp[var] = pd.Series(data['values'])
            if 'chron' in filename.lower():
                dfs['chronData'][filename] = pd.DataFrame(tmp)
            elif 'paleo' in filename.lower():
                dfs['paleoData'][filename] = pd.DataFrame(tmp)
    except KeyError:
        logger_dataframes.warn(
            'get_lipd_cols: AttributeError: expected type dict, given type {}'
            .format(type(csvs)))
    logger_dataframes.info('exit get_lipd_cols')
    return dfs