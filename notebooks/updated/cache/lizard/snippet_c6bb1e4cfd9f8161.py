def print_all_signals(self):
    for o in dir(self):
        obj = getattr(self, o)
        div = False
        for c in dir(obj):
            cobj = getattr(obj, c)
            if isinstance(cobj, Signal):
                print('def _on_{}__{}(self):'.format(o, c))
                div = True
        if div:
            print('-' * 30)