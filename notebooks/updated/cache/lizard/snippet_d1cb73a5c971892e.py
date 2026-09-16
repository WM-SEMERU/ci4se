def normal_fields(self):
    return {f: v for f, v in self.fields.items() if not f.startswith('_')}