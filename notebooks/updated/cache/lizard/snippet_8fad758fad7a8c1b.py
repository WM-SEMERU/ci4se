def relations_to(self, target, include_object=False):
    relations = self._get_item_node(target).incoming
    if include_object:
        for k in relations:
            for v in relations[k]:
                if hasattr(v, 'obj'):
                    yield v.obj, k
    else:
        yield from relations