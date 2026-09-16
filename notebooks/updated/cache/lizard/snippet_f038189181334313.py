def _set_transmaps(self):
    if self._std == 'ascii':
        self._lower_chars = string.ascii_lowercase
        self._upper_chars = string.ascii_uppercase
    elif self._std == 'rfc1459':
        self._lower_chars = string.ascii_lowercase + ''.join(chr(i) for i in
            range(123, 127))
        self._upper_chars = string.ascii_uppercase + ''.join(chr(i) for i in
            range(91, 95))
    elif self._std == 'rfc1459-strict':
        self._lower_chars = string.ascii_lowercase + ''.join(chr(i) for i in
            range(123, 126))
        self._upper_chars = string.ascii_uppercase + ''.join(chr(i) for i in
            range(91, 94))