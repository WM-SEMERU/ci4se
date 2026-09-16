def _delColumn(cat, col):
    if col in cat.schema():
        try:
            cat.delColumn(col)
            logger.info('Column %s deleted from %s.' % (col, cat.id))
            return True
        except:
            logger.error('Catalog column %s error while deleting from %s.' %
                (col, cat.id))
    return False