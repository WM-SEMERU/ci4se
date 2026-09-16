def get_features(self, organism=None, sequence=None):
    data = {}
    data = self._update_data(data, organism, sequence)
    return self.post('getFeatures', data)