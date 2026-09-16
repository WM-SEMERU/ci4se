def notify_update(self, x, y, width, height):
    if not isinstance(x, baseinteger):
        raise TypeError('x can only be an instance of type baseinteger')
    if not isinstance(y, baseinteger):
        raise TypeError('y can only be an instance of type baseinteger')
    if not isinstance(width, baseinteger):
        raise TypeError('width can only be an instance of type baseinteger')
    if not isinstance(height, baseinteger):
        raise TypeError('height can only be an instance of type baseinteger')
    self._call('notifyUpdate', in_p=[x, y, width, height])