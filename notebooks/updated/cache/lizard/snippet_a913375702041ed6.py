def dannotsagg2dannots2dalignbedannot(cfg):
    datatmpd = cfg['datatmpd']
    dannotsagg = del_Unnamed(pd.read_csv(cfg['dannotsaggp'], sep='\t'))
    dalignbedstats = del_Unnamed(pd.read_csv(cfg['dalignbedstatsp'], sep='\t'))
    dalignbedannotp = cfg['dalignbedannotp']
    logging.info(basename(dalignbedannotp))
    if not exists(dalignbedannotp) or cfg['force']:
        dalignbedannot = dalignbedstats.set_index('id').join(set_index(
            dannotsagg, 'id'), rsuffix=' annotation')
        dalignbedannot['NM'] = dalignbedannot['NM'].apply(int)
        dalignbedannot.to_csv(dalignbedannotp, sep='\t')
    return cfg