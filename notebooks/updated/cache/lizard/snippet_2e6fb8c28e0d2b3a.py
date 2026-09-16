def get_value(self):
    df = self.dataModel.get_data()
    if self.is_series:
        return df.iloc[:, (0)]
    else:
        return df