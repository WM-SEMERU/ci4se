def _add_aliases(self, node):
    assert isinstance(node, (ast.Import, ast.ImportFrom))
    for name_and_alias in node.names:
        name = name_and_alias.name.partition('.')[0]
        alias = name_and_alias.asname
        self._define(self.defined_imports, alias or name, node, confidence=
            90, ignore=_ignore_import)
        if alias is not None:
            self.used_names.add(name_and_alias.name)