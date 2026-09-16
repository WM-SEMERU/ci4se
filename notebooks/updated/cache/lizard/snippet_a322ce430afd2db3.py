def transform(self, input_df):
    _df = input_df.copy(deep=False)
    for column in self.cat_columns:
        if column not in _df:
            raise RuntimeError('Required column {:s} not found'.format(column))
        if _df[column].dtype == 'object':
            print('Changing column {:s} to category'.format(column))
            _df[column] = pd.Categorical(_df[column])
    _df = _df.select_dtypes(include=['bool', 'int', 'float', 'category'])
    if self.normalize:
        for column in list(_df.select_dtypes(include=[np.number]).columns.
            values):
            print('Normalizing column {:s}...'.format(column))
            smin, smax = self.norm_map[column]
            _df[column] = (_df[column] - smin) / (smax - smin)
    return self.dummy_encoder.transform(_df)