def typedef_callable_handle(tokens):
    if len(tokens) == 1:
        return '_coconut.typing.Callable[..., ' + tokens[0] + ']'
    elif len(tokens) == 2:
        return '_coconut.typing.Callable[[' + tokens[0] + '], ' + tokens[1
            ] + ']'
    else:
        raise CoconutInternalException('invalid Callable typedef tokens',
            tokens)