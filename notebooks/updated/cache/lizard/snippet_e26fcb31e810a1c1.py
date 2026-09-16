def ignite(self, args=None):
    if args is None:
        args = sys.argv[1:]
    if os.environ.get('MANAGED_VIRTUALENV', None) != '1':
        made = self.make_virtualenv()
        if made or os.environ.get('VENV_STARTER_CHECK_DEPS', None) != '0':
            self.install_deps()
    self.start_program(args)