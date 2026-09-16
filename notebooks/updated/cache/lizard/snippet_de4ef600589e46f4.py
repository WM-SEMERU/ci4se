def print_series_info(self, series_info, minimal_series_number=1):
    strinfo = ''
    if len(series_info) > minimal_series_number:
        for serie_number in series_info.keys():
            strl = get_one_serie_info(series_info, serie_number)
            strinfo = strinfo + strl + '\n'
    return strinfo