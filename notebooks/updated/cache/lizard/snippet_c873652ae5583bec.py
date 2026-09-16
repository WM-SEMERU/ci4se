def run(self, *args):
    params = self.parser.parse_args(args)
    code = self.show(params.uuid, params.term)
    return code