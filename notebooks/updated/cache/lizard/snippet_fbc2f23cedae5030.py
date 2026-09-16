def to_dataframe(self, columns=None):
    if not self.is_value_set:
        raise ValueError('Value must be set before converting to a DataFrame.')
    if not pandas:
        raise RuntimeError('Install pandas to convert to pandas.DataFrame')
    return pandas.DataFrame.from_records(self.value, columns=columns)