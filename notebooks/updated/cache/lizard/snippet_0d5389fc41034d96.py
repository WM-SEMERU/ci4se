def variables(self, include_units=False):
    if include_units:
        return self.data[['variable', 'unit']].drop_duplicates().reset_index(
            drop=True).sort_values('variable')
    else:
        return pd.Series(self.data.variable.unique(), name='variable')