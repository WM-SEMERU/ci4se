def adjoint(self):
    r
    if self.domain.is_real:
        if self.scalar.real == self.scalar:
            return self.scalar.real * RealPart(self.range)
        elif 1.0j * self.scalar.imag == self.scalar:
            return self.scalar.imag * ImagPart(self.range)
        else:
            return self.scalar.real * RealPart(self.range
                ) + self.scalar.imag * ImagPart(self.range)
    else:
        return ComplexEmbedding(self.range, self.scalar.conjugate())