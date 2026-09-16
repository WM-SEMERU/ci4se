def register_variable_compilation(self, path, compilation_cbk, listclass):
    self.compilations_variable[path] = {'callback': compilation_cbk,
        'listclass': listclass}