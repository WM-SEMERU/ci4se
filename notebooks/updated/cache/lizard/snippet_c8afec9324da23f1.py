def setup(self):
    for prefix, routes in self.sub_rt:
        routes.prefix = self.prefix + prefix
        routes.setup()
        fn_name_prefixes = {}
        for fn_key, fn in routes.fn_namespace.items():
            self.fn_namespace[routes.name + '.' + fn_key] = fn
            fn_prefix = routes.name
            if '.' in fn_key:
                fn_prefix += '.' + fn_key.rsplit('.', 1)[0]
            fn_name_prefixes[fn] = fn_prefix
        for key in self:
            funcs = set(rule[1] for rule in self[key])
            for route, route_module, module, fn in routes.get(key, []):
                if fn not in funcs:
                    new_route = Route(prefix + route.path)
                    fn.rw_route = new_route
                    fn_name_prefix = fn_name_prefixes[fn]
                    data = new_route, fn_name_prefix, module, fn
                    self[key].append(data)
    for key in self:
        self[key].sort(key=lambda rule: rule[0])