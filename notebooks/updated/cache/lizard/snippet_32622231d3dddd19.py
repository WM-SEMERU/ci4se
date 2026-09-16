def add(request, kind, method, *args):
    request.session.setdefault(_key_name(kind), []).append({'method':
        method, 'args': args})