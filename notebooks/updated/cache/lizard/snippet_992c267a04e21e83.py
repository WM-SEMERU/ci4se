def load_to_array(self, keys):
    data = np.empty((len(self.data[keys[0]]), len(keys)))
    for i in range(0, len(self.data[keys[0]])):
        for j, key in enumerate(keys):
            data[i, j] = self.data[key][i]
    return data