def orderedclasses(self, set_uri_or_id=None, nestedhierarchy=False):
    classes = self.classes(set_uri_or_id, nestedhierarchy)
    for classid in self.classorder(classes):
        yield classes[classid]