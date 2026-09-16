def starting_expression(source_code, offset):
    word_finder = worder.Worder(source_code, True)
    expression, starting, starting_offset = (word_finder.
        get_splitted_primary_before(offset))
    if expression:
        return expression + '.' + starting
    return starting