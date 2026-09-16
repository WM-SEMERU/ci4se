def checkIsConsistent(self):
    if is_an_array(self.mask) and self.mask.shape != self.data.shape:
        raise ConsistencyError('Shape mismatch mask={}, data={}'.format(
            self.mask.shape != self.data.shape))