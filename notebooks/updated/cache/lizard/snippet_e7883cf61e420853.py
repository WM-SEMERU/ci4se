def pandasdfsummarytojson(df, ndigits=3):
    df = df.transpose()
    return {k: _pandassummarytojson(v, ndigits) for k, v in df.iterrows()}