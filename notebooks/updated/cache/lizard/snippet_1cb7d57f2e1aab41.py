def v_unique_name_children(ctx, stmt):

    def sort_pos(p1, p2):
        if p1.line < p2.line:
            return p1, p2
        else:
            return p2, p1
    dict = {}
    chs = stmt.i_children

    def check(c):
        key = c.i_module.i_modulename, c.arg
        if key in dict:
            dup = dict[key]
            minpos, maxpos = sort_pos(c.pos, dup.pos)
            pos = chk_uses_pos(c, maxpos)
            err_add(ctx.errors, pos, 'DUPLICATE_CHILD_NAME', (stmt.arg,
                stmt.pos, c.arg, minpos))
        else:
            dict[key] = c
        if c.keyword == 'choice':
            for case in c.i_children:
                for cc in case.i_children:
                    check(cc)
    for c in chs:
        check(c)