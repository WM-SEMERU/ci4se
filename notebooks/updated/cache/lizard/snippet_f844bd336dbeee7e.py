def omero_cli(self, command):
    assert isinstance(command, list)
    if not self.cli:
        raise Exception('omero.cli not initialised')
    log.info('Invoking CLI [current environment]: %s', ' '.join(command))
    self.cli.invoke(command, strict=True)