def closing_plugin(self, cancelable=False):
    self.save_config()
    self.explorer.closing_widget()
    return True