def init(self):
    self.logger.info('Start initialize dir [%s]', self.basePath)
    for name in os.listdir(self.basePath):
        path = os.path.join(self.basePath, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
    self.logger.info('Prepare dirs and files')
    for name in self.DIRS:
        os.mkdir(os.path.join(self.basePath, name))
    with open(os.path.join(self.basePath, self.FILE_INDEX), 'wb') as fd:
        pass
    with open(os.path.join(self.basePath, self.FILE_SERIAL), 'wb') as fd:
        print >> fd, 1000
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname
        (os.path.abspath(__file__))), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('openssl.config.template')
    content = template.render(basePath=self.basePath)
    with open(os.path.join(self.basePath, self.FILE_CONFIG), 'wb') as fd:
        print >> fd, content