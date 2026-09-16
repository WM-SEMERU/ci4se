def dbStore(self, typ, py_value):
    if py_value is not None:
        py_value = projex.text.decoded(py_value)
        if self.cleaned():
            py_value = self.clean(py_value)
        if self.escaped():
            py_value = self.escape(py_value)
        return py_value
    else:
        return py_value