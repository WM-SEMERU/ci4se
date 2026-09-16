def on_config_value_changed(self, config_m, prop_name, info):
    config_key = info['args'][1] if 'key' not in info['kwargs'] else info[
        'kwargs']['key']
    self._handle_config_update(config_m, config_key)