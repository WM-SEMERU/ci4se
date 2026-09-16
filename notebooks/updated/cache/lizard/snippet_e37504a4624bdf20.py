def setting(self):
    prog_type = self.__program.program_type
    return self._setting / self.SETTING_DIVIDES[prog_type]