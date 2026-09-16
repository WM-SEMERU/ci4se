async def get_config(self):
    config_facade = client.ModelConfigFacade.from_connection(self.connection())
    result = await config_facade.ModelGet()
    config = result.config
    for key, value in config.items():
        config[key] = ConfigValue.from_json(value)
    return config