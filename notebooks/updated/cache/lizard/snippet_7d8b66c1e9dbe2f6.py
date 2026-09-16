def visit_ImportFrom(self, node):
    line = self._code_lines[node.lineno - 1]
    module_name = line.split('from')[1].split('import')[0].strip()
    for name in node.names:
        imported_name = name.name
        if name.asname:
            imported_name = name.asname + '::' + imported_name
        self.imported_names[imported_name] = module_name