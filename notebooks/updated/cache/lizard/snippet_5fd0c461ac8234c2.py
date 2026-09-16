def intercept_callback_query_origin(fn=pair, origins='all'):
    origin_map = helper.SafeDict()

    def tuplize(fn):

        def tp(msg):
            return fn(msg),
        return tp
    router = helper.Router(tuplize(per_callback_query_origin(origins=
        origins)), origin_map)

    def modify_origin_map(origin, dest, set):
        if set:
            origin_map[origin] = dest
        else:
            try:
                del origin_map[origin]
            except KeyError:
                pass
    if origins == 'all':
        intercept = modify_origin_map
    else:
        intercept = (modify_origin_map if 'chat' in origins else False, 
            modify_origin_map if 'inline' in origins else False)

    @_ensure_seeders_list
    def p(seeders, delegator_factory, *args, **kwargs):
        return fn(seeders + [_wrap_none(router.map)], delegator_factory, *
            args, intercept_callback_query=intercept, **kwargs)
    return p