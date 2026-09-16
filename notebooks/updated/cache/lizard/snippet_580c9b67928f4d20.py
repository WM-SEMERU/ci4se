def repeat_all(self, count=2):
    try:
        return self.__class__(''.join(str(self) * count))
    except TypeError:
        raise TypeError('`count` must be an integer. Got: {!r}'.format(count))