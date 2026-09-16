def print_package_versions(self):
    variants = self.context.get_tool_variants(self.tool_name)
    if variants:
        if len(variants) > 1:
            self._print_conflicting(variants)
            return 1
        else:
            from rez.packages_ import iter_packages
            variant = iter(variants).next()
            it = iter_packages(name=variant.name)
            rows = []
            colors = []
            for pkg in sorted(it, key=lambda x: x.version, reverse=True):
                if pkg.version == variant.version:
                    name = '* %s' % pkg.qualified_name
                    col = heading
                else:
                    name = '  %s' % pkg.qualified_name
                    col = local if pkg.is_local else None
                label = '(local)' if pkg.is_local else ''
                rows.append((name, pkg.path, label))
                colors.append(col)
            _pr = Printer()
            for col, line in zip(colors, columnise(rows)):
                _pr(line, col)
    return 0