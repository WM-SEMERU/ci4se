def str_fraction(self):
    if self.undefined:
        return None
    denominator = locale.format('%d', self.denominator, grouping=True)
    numerator = self.str_numerator.rjust(len(denominator))
    return '{0}/{1}'.format(numerator, denominator)