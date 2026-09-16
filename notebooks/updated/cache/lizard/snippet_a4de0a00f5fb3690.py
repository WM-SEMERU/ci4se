def num_equal(result, operator, comparator):
    if operator == '<':
        return len([x for x in result if x < comparator])
    elif operator == '>':
        return len([x for x in result if x > comparator])
    elif operator == '=':
        return len([x for x in result if x == comparator])
    else:
        raise ValueError