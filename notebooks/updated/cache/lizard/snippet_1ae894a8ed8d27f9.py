def named_tuple_factory(colnames, rows):
    clean_column_names = map(_clean_column_name, colnames)
    try:
        Row = namedtuple('Row', clean_column_names)
    except SyntaxError:
        warnings.warn(
            'Failed creating namedtuple for a result because there were too many columns. This is due to a Python limitation that affects namedtuple in Python 3.0-3.6 (see issue18896). The row will be created with {substitute_factory_name}, which lacks some namedtuple features and is slower. To avoid slower performance accessing values on row objects, Upgrade to Python 3.7, or use a different row factory. (column names: {colnames})'
            .format(substitute_factory_name=pseudo_namedtuple_factory.
            __name__, colnames=colnames))
        return pseudo_namedtuple_factory(colnames, rows)
    except Exception:
        clean_column_names = list(map(_clean_column_name, colnames))
        log.warning(
            'Failed creating named tuple for results with column names %s (cleaned: %s) (see Python \'namedtuple\' documentation for details on name rules). Results will be returned with positional names. Avoid this by choosing different names, using SELECT "<col name>" AS aliases, or specifying a different row_factory on your Session'
             % (colnames, clean_column_names))
        Row = namedtuple('Row', _sanitize_identifiers(clean_column_names))
    return [Row(*row) for row in rows]