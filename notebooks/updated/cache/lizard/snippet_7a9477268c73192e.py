def check(code):

    def safe_lookup(op):
        try:
            return instructions.lookup(op)
        except Exception:
            return op
    for i, a in enumerate(code):
        b = code[i + 1] if i + 1 < len(code) else None
        if not isconstant(a):
            try:
                instructions.lookup(a)
            except KeyError as err:
                if not (len(err.args) == 1 and is_embedded_push(err.args[0])):
                    raise CompileError(
                        'Instruction at index %d is unknown: %s' % (i, a))
        if isstring(a) and safe_lookup(b) == instructions.cast_int:
            raise CompileError(
                'Cannot convert string to integer (index %d): %s %s' % (i,
                a, b))
        boolean_ops = [instructions.boolean_not, instructions.boolean_or,
            instructions.boolean_and]
        if not isbool(a) and safe_lookup(b) in boolean_ops:
            raise CompileError(
                'Can only use binary operators on booleans (index %d): %s %s' %
                (i, a, b))
    return code