def labels(self):
    if self._labels is None:
        cmd = ['skopeo', 'inspect', self.skopeo_target]
        self._labels = json.loads(subprocess.check_output(cmd))['Labels']
    return self._labels