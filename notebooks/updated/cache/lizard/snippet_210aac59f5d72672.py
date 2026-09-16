def update_attributes(self, **kwargs):
    attrs = self.attributes.values() + self.lists.values(
        ) + self.references.values()
    for att in attrs:
        if att.name in kwargs:
            att.__set__(self, kwargs[att.name])