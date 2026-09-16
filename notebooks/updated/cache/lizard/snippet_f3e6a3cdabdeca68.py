def type_complexity(type_):
    if not typing or not isinstance(type_, (typing.TypingMeta,
        GenericWrapperMeta)) or type_ is AnyType:
        return 0
    if issubclass(type_, typing.Union):
        return reduce(operator.or_, map(type_complexity, type_.
            __union_params__))
    if issubclass(type_, typing.Tuple):
        if type_.__tuple_params__ is None:
            return 1
        elif type_.__tuple_use_ellipsis__:
            return 2
        else:
            return 8
    if isinstance(type_, GenericWrapperMeta):
        type_count = 0
        for p in reversed(type_.parameters):
            if type_count > 0:
                type_count += 1
            if p is AnyType:
                continue
            if not isinstance(p, typing.TypeVar
                ) or p.__constraints__ or p.__bound__:
                type_count += 1
        return 1 << min(type_count, 2)
    return 0