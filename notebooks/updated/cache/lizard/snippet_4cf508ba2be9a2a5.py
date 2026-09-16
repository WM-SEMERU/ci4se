def _on_cancel_button_clicked(self, *args):
    self.core_config_model.preliminary_config.clear()
    self.gui_config_model.preliminary_config.clear()
    self.__destroy()