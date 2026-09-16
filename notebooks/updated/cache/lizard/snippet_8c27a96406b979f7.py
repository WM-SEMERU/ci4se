def create_update():
    update = upkey('update').setResultsName('action')
    returns, none, all_, updated, old, new = map(upkey, ['returns', 'none',
        'all', 'updated', 'old', 'new'])
    return_ = returns + Group(none | all_ + old | all_ + new | updated +
        old | updated + new).setResultsName('returns')
    return update + table + update_expr + Optional(keys_in) + Optional(where
        ) + Optional(using) + Optional(return_) + Optional(throttle)