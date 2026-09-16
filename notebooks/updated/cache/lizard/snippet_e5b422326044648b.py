def str_fraction(self):
    if self._eta.undefined:
        return None
    unit_denominator, unit = self._unit_class(self.denominator).auto
    formatter = '%d' if unit_denominator == self.denominator else '%0.2f'
    denominator = locale.format(formatter, unit_denominator, grouping=True)
    unit_numerator = getattr(self._unit_class(self.numerator), unit)
    if self.done:
        rounded_numerator = unit_numerator
    else:
        rounded_numerator = float(Decimal(str(unit_numerator)).quantize(
            Decimal('.01'), rounding=ROUND_DOWN))
    numerator = locale.format(formatter, rounded_numerator, grouping=True
        ).rjust(len(denominator))
    return '{0}/{1} {2}'.format(numerator, denominator, unit)