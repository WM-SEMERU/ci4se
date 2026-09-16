def visit_desc(self):
    desc = []
    if self.__desc__:
        desc += [self.__desc__]
    for node in pe.utils.topological_sort(self._graph)[0]:
        if isinstance(node, LiterateWorkflow):
            add_desc = node.visit_desc()
            if add_desc not in desc:
                desc.append(add_desc)
    if self.__postdesc__:
        desc += [self.__postdesc__]
    return ''.join(desc)