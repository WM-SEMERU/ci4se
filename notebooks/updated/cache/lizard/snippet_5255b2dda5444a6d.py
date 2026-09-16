def query_get_kb_by_type(kbtype):
    return models.KnwKB.query.filter_by(kbtype=models.KnwKB.KNWKB_TYPES[kbtype]
        )