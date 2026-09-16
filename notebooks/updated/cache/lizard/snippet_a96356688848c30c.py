def get_defaults(self):
    options = [copy.copy(opt) for opt in self._options]
    for opt in options:
        try:
            del opt.kwargs['required']
        except KeyError:
            pass
    parser = self.build_parser(options, permissive=True, add_help=False)
    parsed, _ = parser.parse_known_args([])
    return vars(parsed)