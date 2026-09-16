def add_argument(self, parser, bootstrap=False):
    if self.cli_expose:
        if isinstance(self.child, YapconfBoolItem):
            original_default = self.child.default
            self.child.default = True
            args = self.child._get_argparse_names(parser.prefix_chars)
            kwargs = self._get_argparse_kwargs(bootstrap)
            parser.add_argument(*args, **kwargs)
            self.child.default = False
            args = self.child._get_argparse_names(parser.prefix_chars)
            kwargs = self._get_argparse_kwargs(bootstrap)
            parser.add_argument(*args, **kwargs)
            self.child.default = original_default
        else:
            super(YapconfListItem, self).add_argument(parser, bootstrap)