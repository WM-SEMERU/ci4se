def load_SUEWS_Forcing_met_df_pattern(path_input, forcingfile_met_pattern):
    path_input = path_input.resolve()
    list_file_MetForcing = sorted([f for f in path_input.glob(
        forcingfile_met_pattern) if 'ESTM' not in f.name])
    dd_forcing_met = dd.read_csv(list_file_MetForcing, delim_whitespace=
        True, comment='!', error_bad_lines=True)
    df_forcing_met = dd_forcing_met.compute()
    df_forcing_met = df_forcing_met.drop_duplicates()
    col_suews_met_forcing = ['iy', 'id', 'it', 'imin', 'qn', 'qh', 'qe',
        'qs', 'qf', 'U', 'RH', 'Tair', 'pres', 'rain', 'kdown', 'snow',
        'ldown', 'fcld', 'Wuh', 'xsmd', 'lai', 'kdiff', 'kdir', 'wdir']
    df_forcing_met.columns = col_suews_met_forcing
    df_forcing_met['pres'] *= 10
    df_forcing_met['isec'] = 0
    df_forcing_met[['iy', 'id', 'it', 'imin', 'isec']] = df_forcing_met[[
        'iy', 'id', 'it', 'imin', 'isec']].astype(np.int64)
    idx_dt = pd.date_range(*df_forcing_met.iloc[([0, -1]), :4].astype(int).
        astype(str).apply(lambda ser: ser.str.cat(sep=' '), axis=1).map(lambda
        dt: pd.Timestamp.strptime(dt, '%Y %j %H %M')), periods=
        df_forcing_met.shape[0])
    df_forcing_met = df_forcing_met.set_index(idx_dt)
    return df_forcing_met