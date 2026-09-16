def get_first_non_null_value(self, ind_name, col_name):
    short_df = self.df.loc[ind_name, col_name]
    mask = pd.notnull(short_df)
    print(short_df[mask])
    try:
        val = short_df[mask].unique()[0]
    except IndexError:
        val = None
    return val