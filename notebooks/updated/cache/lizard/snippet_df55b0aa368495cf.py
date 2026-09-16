def parse_args(self, args=None, namespace=None, defaults=None):
    epilog = self.subparsers_summary()
    epilog += self.epilog
    return self(RootParser, epilog=epilog).parse_args(args, namespace, defaults
        )