def make_ui(self, path='hgwebdir.config'):
    sections = ['alias', 'auth', 'decode/encode', 'defaults', 'diff',
        'email', 'extensions', 'format', 'merge-patterns', 'merge-tools',
        'hooks', 'http_proxy', 'smtp', 'patch', 'paths', 'profiling',
        'server', 'trusted', 'ui', 'web']
    repos = path
    baseui = ui.ui()
    cfg = config.config()
    cfg.read(repos)
    self.paths = cfg.items('paths')
    self.base_path = self.paths[0][1].replace('*', '')
    self.check_repo_dir(self.paths)
    self.set_statics(cfg)
    for section in sections:
        for k, v in cfg.items(section):
            baseui.setconfig(section, k, v)
    return baseui