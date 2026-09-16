def to_dict(self):
    vars = super(ClassDoc, self).to_dict()
    vars.update({'name': self.name, 'method': [method.to_dict() for method in
        self.methods]})
    return vars