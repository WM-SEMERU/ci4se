def printUnusedImports(self):
    for module in self.listModules():
        names = [(unused.lineno, unused.name) for unused in module.unused_names
            ]
        names.sort()
        for lineno, name in names:
            if not self.all_unused:
                line = linecache.getline(module.filename, lineno)
                if '#' in line:
                    continue
            print('%s:%s: %s not used' % (module.filename, lineno, name))