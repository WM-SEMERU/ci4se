def content_type(self, content_type):
    option = Option()
    option.number = defines.OptionRegistry.CONTENT_TYPE.number
    option.value = int(content_type)
    self.add_option(option)