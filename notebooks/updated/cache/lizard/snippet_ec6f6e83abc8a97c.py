def view(self):
    proxied = get_proxied_expr(self)
    kv = dict((attr, getattr(proxied, attr)) for attr in get_attrs(proxied))
    return type(proxied)(**kv)