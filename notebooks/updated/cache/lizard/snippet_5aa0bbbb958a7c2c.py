def start_with(self, x):
    _args = []
    for arg in self.all:
        if is_collection(x):
            for _x in x:
                if arg.startswith(x):
                    _args.append(arg)
                    break
        elif arg.startswith(x):
            _args.append(arg)
    return Args(_args, no_argv=True)