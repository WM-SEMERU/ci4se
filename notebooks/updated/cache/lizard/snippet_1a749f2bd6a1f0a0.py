def get_stub(self, name, arch):
    proc = self.fallback_proc(display_name=name, is_stub=True)
    self._apply_metadata(proc, arch)
    return proc