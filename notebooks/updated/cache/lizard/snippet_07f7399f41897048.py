def define_help_flags():
    global _define_help_flags_called
    if not _define_help_flags_called:
        flags.DEFINE_flag(HelpFlag())
        flags.DEFINE_flag(HelpshortFlag())
        flags.DEFINE_flag(HelpfullFlag())
        flags.DEFINE_flag(HelpXMLFlag())
        _define_help_flags_called = True