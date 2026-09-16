def set_input(self, data):
    for name, value in data.items():
        i = self.form.find('input', {'name': name})
        if not i:
            raise InvalidFormMethod('No input field named ' + name)
        i['value'] = value