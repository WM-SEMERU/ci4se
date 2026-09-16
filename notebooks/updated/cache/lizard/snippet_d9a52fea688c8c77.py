def get_cwd(self):
    cwd = os.path.dirname(os.path.abspath(self._template_file))
    if self._docker_volume_basedir:
        cwd = self._docker_volume_basedir
    return cwd