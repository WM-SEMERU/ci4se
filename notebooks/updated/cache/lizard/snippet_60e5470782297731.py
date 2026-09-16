def read_csv(*args, **kwargs):
    kwargs.update({'low_memory': False})
    if isinstance(args[0], pd.DataFrame):
        df = args[0]
    else:
        logger.info('Reading CSV with `read_csv(*{}, **{})`...'.format(args,
            kwargs))
        df = pd.read_csv(*args, **kwargs)
    if looks_like_index(df[df.columns[0]]):
        df = df.set_index(df.columns[0], drop=True)
        if df.index.name in ('Unnamed: 0', ''):
            df.index.name = None
    if str(df.index.values.dtype).startswith('int') and (df.index.values > 
        1000000000.0 * 3600 * 24 * 366 * 10).any() or str(df.index.values.dtype
        ) == 'object':
        try:
            df.index = pd.to_datetime(df.index)
        except (ValueError, TypeError, pd.errors.OutOfBoundsDatetime):
            logger.info(
                'Unable to coerce DataFrame.index into a datetime using pd.to_datetime([{},...])'
                .format(df.index.values[0]))
    return df