def mean_values(self):
    vals = self.pst.observation_data.obsval.copy()
    vals.loc[self.names] = 0.0
    return vals