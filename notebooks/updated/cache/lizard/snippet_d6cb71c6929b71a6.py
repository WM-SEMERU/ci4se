def refactor_froms_to_imports(self, offset):
    refactor = ImportOrganizer(self.project)
    changes = refactor.froms_to_imports(self.resource, offset)
    return translate_changes(changes)