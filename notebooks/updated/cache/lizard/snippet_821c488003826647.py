def _replace_nans(self, data):
    for c in data:
        dtype = data[c].dtype
        if dtype in (np.float32, np.float64):
            if dtype == np.float32:
                replacement = self.MISSING_VALUES['f']
            else:
                replacement = self.MISSING_VALUES['d']
            data[c] = data[c].fillna(replacement)
    return data