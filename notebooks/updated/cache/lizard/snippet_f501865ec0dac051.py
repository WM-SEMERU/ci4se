def set_infra_led_config(self, mode, callback=None):
    params = {'mode': mode}
    return self.execute_command('setInfraLedConfig', params, callback=callback)