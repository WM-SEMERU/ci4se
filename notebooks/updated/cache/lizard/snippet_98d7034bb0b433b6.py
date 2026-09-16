def init_argparser(self, argparser):
    super(PackageManagerRuntime, self).init_argparser(argparser)
    actions = argparser.add_argument_group('action arguments')
    count = 0
    for full, short, desc in self.pkg_manager_options:
        args = [(dash + key) for dash, key in zip(('-', '--'), (short, full
            )) if key]
        desc = desc.replace('Python package', 'Python package(s)')
        if not short:
            f = getattr(self.cli_driver, '%s_%s' % (self.cli_driver.binary,
                full), None)
            if callable(f):
                count += 1
                actions.add_argument(*args, help=desc, action=
                    PackageManagerAction, dest=self.action_key, const=(
                    count, f))
                if self.default_action is None:
                    self.default_action = f
                continue
        argparser.add_argument(*args, help=desc, action='store_true')
    argparser.add_argument('package_names', metavar=metavar('package'),
        nargs='+', help=
        "python packages to be used for the generation of '%s'" % (self.
        cli_driver.pkgdef_filename,))