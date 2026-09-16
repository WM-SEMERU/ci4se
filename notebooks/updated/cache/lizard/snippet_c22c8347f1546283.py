def scan_module(self, pkgpath, modpath, node):

    def scan_imports(node):
        if node_type(node) == 'Import':
            for binding in node.names:
                name, asname = binding.name, binding.asname
                if asname:
                    self.add(modpath, asname, name)
                else:
                    top_name = name.split('.')[0]
                    self.add(modpath, top_name, top_name)
                self.add_package_origins(name)
        elif node_type(node) == 'ImportFrom':
            frompath = resolve_frompath(pkgpath, node.module, node.level)
            for binding in node.names:
                name, asname = binding.name, binding.asname
                if name == '*':
                    for name in self.get_star_names(frompath):
                        self.add(modpath, name, frompath + '.' + name)
                    self.add_package_origins(frompath)
                else:
                    self.add(modpath, asname or name, frompath + '.' + name)
                    self.add_package_origins(frompath + '.' + name)
        else:
            for_each_child(node, scan_imports)
    for_each_child(node, scan_imports)