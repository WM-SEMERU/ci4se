def add_column(filename, column, formula, force=False):
    columns = parse_formula(formula)
    logger.info('Running file: %s' % filename)
    logger.debug('  Reading columns: %s' % columns)
    data = fitsio.read(filename, columns=columns)
    logger.debug('  Evaluating formula: %s' % formula)
    col = eval(formula)
    col = np.asarray(col, dtype=[(column, col.dtype)])
    insert_columns(filename, col, force=force)
    return True