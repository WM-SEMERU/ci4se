def normalize_r_value(self):
    if self.r_df is not None and self.r_df.shape[0]:
        self.r_df.r_value = (self.r_df.r_value - self.r_df.r_value.mean()
            ) / self.r_df.r_value.std()