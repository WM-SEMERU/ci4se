def transform(self, column):
    self.check_data_type()
    return pd.DataFrame({self.col_name: np.exp(column[self.col_name])})