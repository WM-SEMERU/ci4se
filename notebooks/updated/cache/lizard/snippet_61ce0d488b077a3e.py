def clone(self):
    base_dir = '/'.join(self.path.split('/')[:-2])
    try:
        os.makedirs(base_dir, 448)
    except OSError:
        pass
    self._cmd(['git', 'clone', self._clone_url, self.path], cwd=os.getcwd())