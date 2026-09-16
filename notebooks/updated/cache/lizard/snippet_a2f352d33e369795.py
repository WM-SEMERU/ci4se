def batting_stats_bref(season=None):
    if season is None:
        season = datetime.datetime.today().strftime('%Y')
    season = str(season)
    start_dt = season + '-03-01'
    end_dt = season + '-11-01'
    return batting_stats_range(start_dt, end_dt)