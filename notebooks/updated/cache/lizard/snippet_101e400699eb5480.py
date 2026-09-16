def FlagValuesDict(self):
    flag_values = {}
    for flag_name in self.RegisteredFlags():
        flag = self.FlagDict()[flag_name]
        flag_values[flag_name] = flag.value
    return flag_values