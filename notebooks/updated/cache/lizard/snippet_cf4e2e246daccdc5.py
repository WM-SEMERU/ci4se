def set_source_interface(self, name):
    cmd = self.command_builder('ntp source', value=name)
    return self.configure(cmd)