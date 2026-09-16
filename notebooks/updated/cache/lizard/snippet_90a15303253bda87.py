def iter_options(self):
    for section in self.sections:
        name = str(section)
        for key, value in section._get_options():
            yield name, key, value