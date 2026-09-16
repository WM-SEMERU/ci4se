def as_rational(self):
    denominator, numerator = NatDivision.undivision(self.integer_part, self
        .non_repeating_part, self.repeating_part, self.base)
    result = Fraction(Nats.convert_to_int(numerator, self.base), Nats.
        convert_to_int(denominator, self.base))
    return result * self.sign