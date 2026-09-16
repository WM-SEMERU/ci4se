def update_embedded(self, attribute):
    coll = self.collection(attribute)
    keys = list(coll.keys())
    for key in keys:
        element = coll[key]
        new_parent = self.find_embedded_parent(element)
        if new_parent is not None:
            element.parent = new_parent
            if attribute == 'types':
                new_parent.types[key] = element
            else:
                new_parent.executables[key] = element
            del coll[key]