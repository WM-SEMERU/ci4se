def doc_dict(self):
    doc = {'type': self.__class__.__name__, 'description': self.description,
        'default': self.default, 'required': self.required}
    if hasattr(self, 'details'):
        doc['detailed_description'] = self.details
    return doc