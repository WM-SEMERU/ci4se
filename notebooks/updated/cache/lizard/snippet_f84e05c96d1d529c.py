def check_classes(self, scope=-1):
    for entry in self[scope].values():
        if entry.class_ is None:
            syntax_error(entry.lineno, "Unknown identifier '%s'" % entry.name)