def get_objects_by_type_in_subtree(self, *types):
    typed_objects = self.get_objects_by_type(*types)
    for child in self.objects.values():
        typed_objects += child.get_objects_by_type_in_subtree(*types)
    return typed_objects