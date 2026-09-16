def load_dataframe(fobj, compression='gzip'):
    try:
        from pandas import read_fwf
    except ImportError:
        raise ImportError(PANDAS_MESSAGE)
    names, colspecs = zip(('hip', (2, 14)), ('magnitude', (41, 46)), (
        'ra_degrees', (51, 63)), ('dec_degrees', (64, 76)), ('parallax_mas',
        (79, 86)), ('ra_mas_per_year', (87, 95)), ('dec_mas_per_year', (96,
        104)))
    df = read_fwf(fobj, colspecs, names=names, compression=compression)
    df = df.assign(ra_hours=df['ra_degrees'] / 15.0, epoch_year=1991.25)
    return df.set_index('hip')