def store(self, w=None, dw=None, pw=None, return_body=True, if_none_match=
    False, timeout=None):
    if len(self.siblings) != 1:
        raise ConflictError(
            'Attempting to store an invalid object, resolve the siblings first'
            )
    self.client.put(self, w=w, dw=dw, pw=pw, return_body=return_body,
        if_none_match=if_none_match, timeout=timeout)
    return self