def is_module(self, name):
    if self.module_prefix.startswith(self.mount_prefix):
        return name.startswith(self.module_prefix)
    return name.startswith(self.module_prefix) and not name.startswith(self
        .mount_prefix)