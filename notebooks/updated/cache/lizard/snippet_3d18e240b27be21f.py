def raise_invalid_type_exception(self):
    message = ('Expecting element type of %s' % self._parameter.
        element_type.__name__)
    err = ValueError(message)
    return err