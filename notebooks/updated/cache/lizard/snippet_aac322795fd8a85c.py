def expression_list_to_conjunction(expression_list):
    if not isinstance(expression_list, list):
        raise AssertionError('Expected `list`, Received {}.'.format(
            expression_list))
    if len(expression_list) == 0:
        return TrueLiteral
    if not isinstance(expression_list[0], Expression):
        raise AssertionError(
            'Non-Expression object {} found in expression_list'.format(
            expression_list[0]))
    if len(expression_list) == 1:
        return expression_list[0]
    else:
        return BinaryComposition('&&', expression_list_to_conjunction(
            expression_list[1:]), expression_list[0])