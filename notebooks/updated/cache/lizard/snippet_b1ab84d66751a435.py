def observe(self, ob):
    option = Option()
    option.number = defines.OptionRegistry.OBSERVE.number
    option.value = ob
    self.del_option_by_number(defines.OptionRegistry.OBSERVE.number)
    self.add_option(option)