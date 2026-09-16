def _load_pickle(self, filename):
    with open(filename, 'rb') as file_handle:
        self._sensors.update(pickle.load(file_handle))