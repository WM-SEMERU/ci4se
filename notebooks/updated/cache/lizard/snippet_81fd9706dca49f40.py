def remove_obsolete_items(self):
    self.rdata = [(filename, data) for filename, data in self.rdata if
        is_module_or_package(filename)]