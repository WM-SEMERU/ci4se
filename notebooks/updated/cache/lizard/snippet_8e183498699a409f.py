def decode_solution(self, encoded_solution):
    return self._decode_function(encoded_solution, *self._decode_args, **
        self._decode_kwargs)