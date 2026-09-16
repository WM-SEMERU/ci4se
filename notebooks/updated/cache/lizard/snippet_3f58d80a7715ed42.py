def copy_assets(self, path='assets'):
    path = os.path.join(self.root_path, path)
    for root, _, files in os.walk(path):
        for file in files:
            fullpath = os.path.join(root, file)
            relpath = os.path.relpath(fullpath, path)
            copy_to = os.path.join(self._get_dist_path(relpath, directory=
                'assets'))
            LOG.debug('copying %r to %r', fullpath, copy_to)
            shutil.copyfile(fullpath, copy_to)