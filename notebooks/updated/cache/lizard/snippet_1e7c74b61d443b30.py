def set_expr(self, ctx):
    if self.readonly:
        raise MuvError("Cannot assign value to constant '%s'." % self.
            varname, position=self.position)
    if self.declare:
        varname = ctx.declare_variable(self.varname)
        if len(self.indexing) == 0:
            return 'var! {var}'.format(var=varname)
    else:
        varname = ctx.lookup_variable(self.varname)
        if varname is None:
            raise MuvError("Undeclared identifier '%s'." % self.varname,
                position=self.position)
    if len(self.indexing) == 0:
        if ctx.assign_level > 1:
            return 'dup {var} !'.format(var=varname)
        else:
            return '{var} !'.format(var=varname)
    if len(self.indexing) == 1:
        if ctx.target in ['fb7']:
            if ctx.assign_level > 1:
                fmt = 'dup {var} @ {idx} ->[] pop'
            else:
                fmt = '{var} @ {idx} ->[] pop'
        elif ctx.assign_level > 1:
            fmt = 'dup {var} @ {idx} ->[] {var} !'
        else:
            fmt = '{var} @ {idx} ->[] {var} !'
        return fmt.format(var=varname, idx=self.indexing[0].generate_code(ctx))
    if ctx.target in ['fb7']:
        if ctx.assign_level > 1:
            fmt = 'dup {var} @ {{ {idx} }}list array_nested_set pop'
        else:
            fmt = '{var} @ {{ {idx} }}list array_nested_set pop'
    elif ctx.assign_level > 1:
        fmt = 'dup {var} @ {{ {idx} }}list array_nested_set {var} !'
    else:
        fmt = '{var} @ {{ {idx} }}list array_nested_set {var} !'
    return fmt.format(var=varname, idx=' '.join(x.generate_code(ctx) for x in
        self.indexing))