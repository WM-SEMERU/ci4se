def register_structure_hook(self, cl, func):
    if is_union_type(cl):
        self._union_registry[cl] = func
    else:
        self._structure_func.register_cls_list([(cl, func)])