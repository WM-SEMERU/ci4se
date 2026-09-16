def is_homogeneous(self):
    hom_base = isinstance(self.base_value, (int, long, numpy.integer, float,
        bool)) or type(self.base_value) == self.dtype or isinstance(self.
        dtype, type) and isinstance(self.base_value, self.dtype)
    hom_ops = all(obj.is_homogeneous for f, obj in self.operations if
        isinstance(obj, larray))
    return hom_base and hom_ops