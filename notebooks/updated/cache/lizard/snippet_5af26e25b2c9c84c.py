def set_textarea(self, data):
    for name, value in data.items():
        t = self.form.find('textarea', {'name': name})
        if not t:
            raise InvalidFormMethod('No textarea named ' + name)
        t.string = value