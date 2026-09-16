async def set_config(self, config):
    config_facade = client.ModelConfigFacade.from_connection(self.connection())
    for key, value in config.items():
        if isinstance(value, ConfigValue):
            config[key] = value.value
    await config_facade.ModelSet(config)