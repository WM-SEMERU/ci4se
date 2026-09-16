def reload(self):
    self._load_data(self.objects.data().filter(key=self.key)[0][0], True)