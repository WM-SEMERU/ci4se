def check(mod):
    v = Check()
    v.visit(mod)
    for t in v.types:
        if t not in mod.types and not t in builtin_types:
            v.errors += 1
            uses = ', '.join(v.types[t])
            print('Undefined type {}, used in {}'.format(t, uses))
    return not v.errors