def add_if_none_match(self):
    option = Option()
    option.number = defines.OptionRegistry.IF_NONE_MATCH.number
    option.value = None
    self.add_option(option)