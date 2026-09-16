def count_missing(self, data, output='number'):
    count = self._find_missing(data, return_bool=False).sum()
    if output == 'number':
        return count
    elif output == 'percent':
        return count / data.shape[0] * 100