def create(self, ami, count, config=None):
    return self.Launcher(config=config).launch(ami, count)