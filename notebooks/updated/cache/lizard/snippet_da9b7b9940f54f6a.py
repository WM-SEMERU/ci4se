def append(self, value):
    if not self.need_free:
        raise ValueError('Stack is read-only')
    if not isinstance(value, X509):
        raise TypeError('StackOfX509 can contain only X509 objects')
    sk_push(self.ptr, libcrypto.X509_dup(value.cert))