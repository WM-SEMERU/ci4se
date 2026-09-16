def publish(self, value):
    value = super(Integer, self).publish(value)
    if isinstance(value, float):
        value = int(value)
    if not isinstance(value, (int, long)):
        raise ValueError('Not an integer: %r' % (value,))
    return value