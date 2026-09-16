def _init(self, parser):
    assert isinstance(parser, argparse.ArgumentParser)
    self._init_parser(parser)
    self._attach_arguments()
    self._attach_subcommands()
    self.initialized = True