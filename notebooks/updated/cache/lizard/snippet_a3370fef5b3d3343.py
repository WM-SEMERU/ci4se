def add_var_condor_cmd(self, command):
    if command not in self.__var_cmds:
        self.__var_cmds.append(command)
        macro = self.__bad_macro_chars.sub('', command)
        self.add_condor_cmd(command, '$(macro' + macro + ')')