def add_transmute_route(self, *args):
    if len(args) == 1:
        fn = args[0]
    elif len(args) == 3:
        methods, paths, fn = args
        fn = describe(methods=methods, paths=paths)(fn)
    else:
        raise ValueError(
            'expected one or three arguments for add_transmute_route!')
    add_route(self._app, fn, context=self._transmute_context)