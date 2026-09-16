def count(self, files=False):
    return len(self.files) if files else len(self.unique())