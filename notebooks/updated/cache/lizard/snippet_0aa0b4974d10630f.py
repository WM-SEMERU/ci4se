def Similarity(self, value=None):
    if value is None:
        value = 0.0
    return Similarity(value, threshold=self.threshold)