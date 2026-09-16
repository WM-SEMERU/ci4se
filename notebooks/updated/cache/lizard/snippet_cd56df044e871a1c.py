def find_prev_keyword(sql):
    if not sql.strip():
        return None, ''
    parsed = sqlparse.parse(sql)[0]
    flattened = list(parsed.flatten())
    logical_operators = 'AND', 'OR', 'NOT', 'BETWEEN'
    for t in reversed(flattened):
        if t.value == '(' or t.is_keyword and t.value.upper(
            ) not in logical_operators:
            idx = flattened.index(t)
            text = ''.join(tok.value for tok in flattened[:idx + 1])
            return t, text
    return None, ''