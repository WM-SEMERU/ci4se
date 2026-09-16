def get_var_shape(self, name):
    rank = self.get_var_rank(name)
    name = create_string_buffer(name)
    arraytype = ndpointer(dtype='int32', ndim=1, shape=(MAXDIMS,), flags='F')
    shape = np.empty((MAXDIMS,), dtype='int32', order='F')
    self.library.get_var_shape.argtypes = [c_char_p, arraytype]
    self.library.get_var_shape(name, shape)
    return tuple(shape[:rank])