def _generate_legacy_type_checks(types=()):
    types = dict(types)

    def gen_type_check(pytypes):
        pytypes = _utils.flatten(pytypes)

        def type_check(checker, instance):
            if isinstance(instance, bool):
                if bool not in pytypes:
                    return False
            return isinstance(instance, pytypes)
        return type_check
    definitions = {}
    for typename, pytypes in iteritems(types):
        definitions[typename] = gen_type_check(pytypes)
    return definitions