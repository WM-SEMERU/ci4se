def get_locals(f):
    return pformat({i: f.f_locals[i] for i in f.f_locals if not i.
        startswith('__')})