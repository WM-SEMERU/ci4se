def set_index(self, index):
    for df in self.get_DataFrame(data=True, with_population=False):
        df.index = index