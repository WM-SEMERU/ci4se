def get_parser(self, **kwargs):
    self.parser = argparse.ArgumentParser(prog=self.prog_name, description=
        self._desc, add_help=False, **kwargs)
    if self.use_config_file:
        self.parser.add_argument('--config-file', action='store', help=
            'Other configuration file.')
    return self.parser