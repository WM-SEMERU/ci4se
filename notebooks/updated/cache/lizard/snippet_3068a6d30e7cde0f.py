def line_plot(self, x='year', y='value', **kwargs):
    df = self.as_pandas(with_metadata=kwargs)
    variables = df['variable'].unique()
    if x in variables or y in variables:
        keep_vars = set([x, y]) & set(variables)
        df = df[df['variable'].isin(keep_vars)]
        idx = list(set(df.columns) - set(['value']))
        df = df.reset_index().set_index(idx).value.unstack(level='variable'
            ).rename_axis(None, axis=1).reset_index().set_index(META_IDX)
        if x != 'year' and y != 'year':
            df = df.drop('year', axis=1)
    ax, handles, labels = plotting.line_plot(df.dropna(), x=x, y=y, **kwargs)
    return ax