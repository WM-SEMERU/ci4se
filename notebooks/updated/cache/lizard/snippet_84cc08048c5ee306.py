def _initIndexDir(self):
    if not os.path.exists(self.logdir):
        os.mkdir(self.logdir)
        dprint(1, 'created', self.logdir)
    Purr.RenderIndex.initIndexDir(self.logdir)