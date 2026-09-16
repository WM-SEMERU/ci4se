def get_modifications(self):
    for modtype, modclass in modtype_to_modclass.items():
        if modtype == 'modification':
            continue
        stmts = self._get_generic_modification(modclass)
        self.statements += stmts