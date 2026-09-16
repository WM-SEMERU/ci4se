def _int_values(self, shape):
    return self.state.randint(low=0, high=100, size=shape).astype('int64')