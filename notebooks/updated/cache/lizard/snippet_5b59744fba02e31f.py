def search_grouping(stmt, name):
    mod = stmt.i_orig_module
    while stmt is not None:
        if name in stmt.i_groupings:
            g = stmt.i_groupings[name]
            if (mod is not None and mod != g.i_orig_module and g.
                i_orig_module.keyword == 'submodule'):
                if mod.search_one('include', g.i_orig_module.arg) is None:
                    return None
            return g
        stmt = stmt.parent
    return None