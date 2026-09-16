def del_expr(self, ctx):
    if self.readonly:
        raise MuvError("Cannot assign value to constant '%s'." % self.
            varname, position=self.position)
    varname = ctx.lookup_variable(self.varname)
    if varname is None:
        raise MuvError("Undeclared identifier '%s'." % self.varname,
            position=self.position)
    if len(self.indexing) == 0:
        return '0 {var} !'.format(var=varname)
    if len(self.indexing) == 1:
        if ctx.target in ['fb7']:
            return '{var} @ {idx} array_delitem'.format(var=varname, idx=
                self.indexing[0].generate_code(ctx))
        else:
            return '{var} @ {idx} array_delitem dup {var} !'.format(var=
                varname, idx=self.indexing[0].generate_code(ctx))
    if ctx.target in ['fb7']:
        return '{var} @ {{ {idx} }}list array_nested_del'.format(var=
            varname, idx=' '.join(x.generate_code(ctx) for x in self.indexing))
    else:
        return '{var} @ {{ {idx} }}list array_nested_del dup {var} !'.format(
            var=varname, idx=' '.join(x.generate_code(ctx) for x in self.
            indexing))