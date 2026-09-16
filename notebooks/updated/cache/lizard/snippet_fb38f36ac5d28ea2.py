def get_translatable_children(self, obj):
    collector = NestedObjects(using='default')
    collector.collect([obj])
    object_list = collector.nested()
    items = self.get_elements(object_list)
    return items[1:]