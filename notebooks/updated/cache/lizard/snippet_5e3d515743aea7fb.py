def cleanup(self):
    for key in self.result:
        self.result[key] = self.result[key].copy()
    for key in list(self._finalizers.keys()):
        self._finalizers[key].clean()