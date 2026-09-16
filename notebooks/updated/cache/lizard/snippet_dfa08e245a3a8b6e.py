def _on_checkbox_toggled(self, renderer, path, config_m, config_list_store):
    config_key = config_list_store[int(path)][self.KEY_STORAGE_ID]
    config_value = bool(config_list_store[int(path)][self.
        TOGGLE_VALUE_STORAGE_ID])
    config_value ^= True
    config_m.set_preliminary_config_value(config_key, config_value)