def allow_constructor(target):
    if not isinstance(target, ClassDouble):
        raise ConstructorDoubleError(
            'Cannot allow_constructor of {} since it is not a ClassDouble.'
            .format(target))
    return allow(target)._doubles__new__