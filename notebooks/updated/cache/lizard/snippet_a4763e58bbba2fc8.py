def set_display_config(cls, config):
    cls.DISPLAY_CONFIG = DisplayConfig(show_approx_str=config.
        show_approx_str, base_config=config.base_config, digits_config=
        config.digits_config, strip_config=config.strip_config)