def to_pandas(self):
    dataframe = self.get().to_pandas()
    assert type(dataframe) is pandas.DataFrame or type(dataframe
        ) is pandas.Series
    return dataframe