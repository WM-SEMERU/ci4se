def get_parameters(self, index):
    if index < 0 or index >= len(self._types):
        raise ValueError(
            'Index for getting parameters associated with order parameter calculation out-of-bounds!'
            )
    return self._params[index]