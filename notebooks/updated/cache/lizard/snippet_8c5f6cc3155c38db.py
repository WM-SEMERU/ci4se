def median(self, func=lambda x: x):
    if self.count() == 0:
        raise NoElementsError('Iterable contains no elements')
    result = self.order_by(func).select(func).to_list()
    length = len(result)
    i = int(length / 2)
    return result[i] if length % 2 == 1 else (float(result[i - 1]) + float(
        result[i])) / float(2)