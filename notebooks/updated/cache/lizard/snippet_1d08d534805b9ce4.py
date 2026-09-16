def get_property(self, index, doctype, name):
    return self.indices[index][doctype].properties[name]