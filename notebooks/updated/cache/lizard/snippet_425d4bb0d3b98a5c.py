def binary(self, name, flag):
    if self.meta.rsl_deps in ['on', 'ON'] and '--resolve-off' not in flag:
        sys.setrecursionlimit(10000)
        dependencies = []
        requires = Requires(name, self.repo).get_deps()
        if requires:
            for req in requires:
                status(0)
                if req and req not in self.black:
                    dependencies.append(req)
            if dependencies:
                self.dep_results.append(dependencies)
                for dep in dependencies:
                    self.binary(dep, flag)
        return self.dep_results
    else:
        return []