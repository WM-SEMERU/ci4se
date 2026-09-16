def trend_coefficients(self, order=LINEAR):
    if not len(self.points):
        raise ArithmeticError('Cannot calculate the trend of an empty series')
    return LazyImport.numpy().polyfit(self.timestamps, self.values, order)