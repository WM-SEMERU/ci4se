def reverse_transform(self, column):
    self.check_data_type()
    return pd.DataFrame({self.col_name: np.log(column[self.col_name])})