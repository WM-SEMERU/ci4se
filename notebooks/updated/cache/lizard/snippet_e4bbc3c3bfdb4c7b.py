def _find_file(self, load):
    path = load.get('path')
    if not path:
        return {'path': '', 'rel': ''}
    tgt_env = load.get('saltenv', 'base')
    return self.find_file(path, tgt_env)