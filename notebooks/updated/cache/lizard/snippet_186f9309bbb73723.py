def histogram_hour_counts(df, variable):
    if not df.index.dtype in ['datetime64[ns]', '<M8[ns]', '>M8[ns]']:
        log.error('index is not datetime')
        return False
    counts = df.groupby(df.index.hour)[variable].count()
    counts.plot(kind='bar', width=1, rot=0, alpha=0.7)