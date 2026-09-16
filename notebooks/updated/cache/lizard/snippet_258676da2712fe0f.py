def iter_symbols(code):
    for name in code.co_names:
        yield name
    for const in code.co_consts:
        if isinstance(const, six.string_types):
            yield const
        elif isinstance(const, CodeType):
            for name in iter_symbols(const):
                yield name