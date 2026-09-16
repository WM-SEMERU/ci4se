def save_codeobject(self, obj):
    if PY3:
        args = (obj.co_argcount, obj.co_kwonlyargcount, obj.co_nlocals, obj
            .co_stacksize, obj.co_flags, obj.co_code, obj.co_consts, obj.
            co_names, obj.co_varnames, obj.co_filename, obj.co_name, obj.
            co_firstlineno, obj.co_lnotab, obj.co_freevars, obj.co_cellvars)
    else:
        args = (obj.co_argcount, obj.co_nlocals, obj.co_stacksize, obj.
            co_flags, obj.co_code, obj.co_consts, obj.co_names, obj.
            co_varnames, obj.co_filename, obj.co_name, obj.co_firstlineno,
            obj.co_lnotab, obj.co_freevars, obj.co_cellvars)
    self.save_reduce(types.CodeType, args, obj=obj)