def set_attr(self):
    setattr(self.attrs, self.kind_attr, self.values)
    setattr(self.attrs, self.meta_attr, self.meta)
    if self.dtype is not None:
        setattr(self.attrs, self.dtype_attr, self.dtype)