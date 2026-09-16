def inverse(self):
    sign = '+' if self.sign == '-' else '-'
    return DiscreteFourierTransformInverse(domain=self.range, range=self.
        domain, axes=self.axes, halfcomplex=self.halfcomplex, sign=sign)