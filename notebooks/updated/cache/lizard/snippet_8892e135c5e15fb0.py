def _realpart(self, f):

    def f_re(x, **kwargs):
        result = np.asarray(f(x, **kwargs), dtype=self.scalar_out_dtype)
        return result.real
    if is_real_dtype(self.out_dtype):
        return f
    else:
        return self.real_space.element(f_re)