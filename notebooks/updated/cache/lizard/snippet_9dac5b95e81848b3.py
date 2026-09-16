def similarity(self, other):
    ratio = SequenceMatcher(a=self.value, b=other.value).ratio()
    similarity = self.Similarity(ratio)
    return similarity