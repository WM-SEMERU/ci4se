def datatable_df(self):
    data = self._all_datatable_data()
    adf = pd.DataFrame(data)
    adf.columns = self.dt_all_cols
    return self._finish_df(adf, 'ALL')