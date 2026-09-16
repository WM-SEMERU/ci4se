def virt_env(self):
    if self._virt_env is None:
        self._virt_env = self._create_virt_env()
    return self._virt_env