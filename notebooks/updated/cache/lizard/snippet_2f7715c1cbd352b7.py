def save_csv(self):
    self.results.sort_values(by=self.column_ids, inplace=True)
    self.results.reindex(columns=self.column_ids).to_csv(self.csv_filepath,
        index=False)