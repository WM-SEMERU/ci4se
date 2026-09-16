def _has_population_germline(rec):
    for k in population_keys:
        if k in rec.header.info:
            return True
    return False