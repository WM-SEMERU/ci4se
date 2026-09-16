def pkg_tracking(self):
    flag = []
    options = ['-t', '--tracking']
    additional_options = ['--check-deps', '--graph=', '--case-ins']
    for arg in self.args[2:]:
        if arg.startswith(additional_options[1]):
            flag.append(arg)
            self.args.remove(arg)
        if arg in additional_options:
            flag.append(arg)
    for f in flag:
        if f in self.args:
            self.args.remove(f)
    for arg in self.args:
        if arg.startswith('--'):
            if arg not in additional_options:
                usage('')
                raise SystemExit()
    if len(self.args) >= 3 and len(self.args) <= 3 and self.args[0
        ] in options and self.args[1] in self.meta.repositories:
        TrackingDeps(self.args[2], self.args[1], flag).run()
    elif len(self.args) >= 2 and self.args[1] not in self.meta.repositories:
        usage(self.args[1])
    else:
        usage('')