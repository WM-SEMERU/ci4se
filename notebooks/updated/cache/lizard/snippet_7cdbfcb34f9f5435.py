def to_pandas_dataframe(self, sample_column=False):
    import pandas as pd
    if sample_column:
        df = pd.DataFrame(self.data(sorted_by=None, sample_dict_cast=True))
    else:
        df = pd.DataFrame(self.record.sample, columns=self.variables)
        for field in sorted(self.record.dtype.fields):
            if field == 'sample':
                continue
            df.loc[:, (field)] = self.record[field]
    return df