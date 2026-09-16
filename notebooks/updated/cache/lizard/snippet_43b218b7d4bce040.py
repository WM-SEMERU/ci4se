def _initialize_with_array(self, data, rowBased=True):
    if rowBased:
        self.matrix = []
        if len(data) != self._rows:
            raise ValueError('Size of Matrix does not match')
        for col in xrange(self._columns):
            self.matrix.append([])
            for row in xrange(self._rows):
                if len(data[row]) != self._columns:
                    raise ValueError('Size of Matrix does not match')
                self.matrix[col].append(data[row][col])
    else:
        if len(data) != self._columns:
            raise ValueError('Size of Matrix does not match')
        for col in data:
            if len(col) != self._rows:
                raise ValueError('Size of Matrix does not match')
        self.matrix = copy.deepcopy(data)