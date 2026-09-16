def _checkout(self):
    cmd = ['atomic', 'mount', '--storage', 'ostree', self.ref_image_name,
        self.mount_point]
    self._run_and_log(cmd, self.ostree_path,
        'Failed to mount selected image as an ostree repo.')