def is_base_tuple(type_str):
    try:
        abi_type = grammar.parse(type_str)
    except exceptions.ParseError:
        return False
    return isinstance(abi_type, grammar.TupleType) and abi_type.arrlist is None