def search_dependencies(self):
    result = [p.dependency() for p in self.ordered_parameters]
    result.extend([v.dependency() for k, v in list(self.members.items())])
    for ekey, anexec in list(self.executables.items()):
        result.extend(anexec.search_dependencies())
    return [m for m in result if m is not None and m != self.module.name]