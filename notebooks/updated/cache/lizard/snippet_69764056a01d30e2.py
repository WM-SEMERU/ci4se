def evaluate(self, sequence):
    last_cache_index = self.cache_scan()
    transformations = self.transformations[last_cache_index:]
    return self.engine.evaluate(sequence, transformations)