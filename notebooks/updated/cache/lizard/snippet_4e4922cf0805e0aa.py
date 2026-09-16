def prepend_rez_path(self):
    if system.rez_bin_path:
        self.env.PATH.prepend(system.rez_bin_path)