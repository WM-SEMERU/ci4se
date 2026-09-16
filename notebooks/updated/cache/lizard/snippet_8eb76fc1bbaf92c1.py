def perform_exe_expansion(self):
    if self.has_section('executables'):
        for option, value in self.items('executables'):
            newStr = self.interpolate_exe(value)
            if newStr != value:
                self.set('executables', option, newStr)