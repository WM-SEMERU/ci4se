def convolved(iterable, kernel_size=1, stride=1, padding=0, default_value=None
    ):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Can't iterate on object.".format(iterable))
    if stride < 1:
        raise ValueError('Stride must be of at least one. Got `stride={}`.'
            .format(stride))
    if not (padding in ['SAME', 'VALID'] or type(padding) in [int]):
        raise ValueError(
            'Padding must be an integer or a string with value `SAME` or `VALID`.'
            )
    if not isinstance(padding, str):
        if padding < 0:
            raise ValueError(
                'Padding must be of at least zero. Got `padding={}`.'.
                format(padding))
    elif padding == 'SAME':
        padding = kernel_size // 2
    elif padding == 'VALID':
        padding = 0
    if not type(iterable) == list:
        iterable = list(iterable)
    if padding > 0:
        pad = [default_value] * padding
        iterable = pad + list(iterable) + pad
    remainder = (kernel_size - len(iterable)) % stride
    extra_pad = [default_value] * remainder
    iterable = iterable + extra_pad
    i = 0
    while True:
        if i > len(iterable) - kernel_size:
            break
        yield iterable[i:i + kernel_size]
        i += stride