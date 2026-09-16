def the_one(cls):
    if cls.THE_ONE is None:
        cls.THE_ONE = cls(settings.HELP_TOKENS_INI_FILE)
    return cls.THE_ONE