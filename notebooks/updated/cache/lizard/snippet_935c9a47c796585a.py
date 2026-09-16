def serialize(self):
    cases = [case.serialize() for key, case in six.iteritems(self.cases)]
    specs = [spec.serialize() for spec in self.describes]
    converted_dict = {'id': self.id, 'name': self.name, 'class_path': self.
        real_class_path, 'doc': self.doc, 'cases': cases, 'specs': specs}
    return converted_dict