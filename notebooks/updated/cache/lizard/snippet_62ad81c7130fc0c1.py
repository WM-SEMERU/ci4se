def select_options(self, options_prefix):
    return WConfigSelection(self.config(), self.section(), self.
        option_prefix() + options_prefix)