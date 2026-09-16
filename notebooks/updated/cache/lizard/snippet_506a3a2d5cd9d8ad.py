def _parse_from_file(self, filepath, fname, dependencies, recursive, greedy):
    string = self.tramp.read(filepath)
    pmodules = self.modulep.parse(string, self, filepath=filepath)
    file_mtime = self._get_mod_mtime(filepath)
    for module in pmodules:
        module.change_time = file_mtime
        self.modules[module.name.lower()] = module
        self._modulefiles[fname].append(module.name.lower())
    pprograms = self.modulep.parse(string, self, False)
    for program in pprograms:
        program.change_time = file_mtime
        self.programs[program.name.lower()] = program
        self._programfiles[fname].append(program.name.lower())
    self._parse_docstrings(filepath)
    return pmodules, pprograms