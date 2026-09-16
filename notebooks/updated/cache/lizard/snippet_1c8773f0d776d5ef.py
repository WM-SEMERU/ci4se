def __parse_args(self, accept_unrecognized_args=False):
    if self.description:
        self.argparser.description = self.description
    elif getattr(sys.modules['__main__'], '__doc__', None):
        self.argparser.description = getattr(sys.modules['__main__'], '__doc__'
            )
    else:
        self.argparser.description = (
            'No documentation defined. Please add a doc string to %s' % sys
            .modules['__main__'].__file__)
    self.argparser.epilog = self.epilog
    if len(sys.argv) == 1 and self.argument_defaults:
        self.argparser.set_defaults(**self.argument_defaults)
    if accept_unrecognized_args:
        self.args, self.unrecognized_args = self.argparser.parse_known_args()
    else:
        self.args = self.argparser.parse_args()