def _get_dmi(cls, df):
    df['pdi'] = cls._get_pdi(df, 14)
    df['mdi'] = cls._get_mdi(df, 14)
    df['dx'] = cls._get_dx(df, 14)
    df['adx'] = df['dx_6_ema']
    df['adxr'] = df['adx_6_ema']