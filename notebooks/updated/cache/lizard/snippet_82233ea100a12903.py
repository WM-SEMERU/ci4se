def validate_abi(abi):
    if not is_list_like(abi):
        raise ValueError("'abi' is not a list")
    if not all(is_dict(e) for e in abi):
        raise ValueError("'abi' is not a list of dictionaries")
    functions = filter_by_type('function', abi)
    selectors = groupby(compose(encode_hex, function_abi_to_4byte_selector),
        functions)
    duplicates = valfilter(lambda funcs: len(funcs) > 1, selectors)
    if duplicates:
        raise ValueError(
            'Abi contains functions with colliding selectors. Functions {0}'
            .format(_prepare_selector_collision_msg(duplicates)))