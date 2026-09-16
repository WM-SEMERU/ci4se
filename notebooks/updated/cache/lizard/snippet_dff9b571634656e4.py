def execute(self, *args, **kwargs):
    args = self.parser.parse_args(*args, **kwargs)
    self.process(args)