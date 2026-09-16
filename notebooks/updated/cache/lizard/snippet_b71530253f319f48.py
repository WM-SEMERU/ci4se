def adjoint(self):
    if self.variant == 'dirac':
        variant = 'point_eval'
    elif self.variant == 'char_fun':
        variant = 'integrate'
    else:
        raise RuntimeError('The variant "{!r}" is not yet supported'.format
            (self.variant))
    return SamplingOperator(self.range, self.sampling_points, variant)