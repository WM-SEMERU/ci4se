def set_select(self, data):
    for name, value in data.items():
        select = self.form.find('select', {'name': name})
        if not select:
            raise InvalidFormMethod('No select named ' + name)
        for option in select.find_all('option'):
            if 'selected' in option.attrs:
                del option.attrs['selected']
        if not isinstance(value, list) and not isinstance(value, tuple):
            value = value,
        elif 'multiple' not in select.attrs:
            raise LinkNotFoundError('Cannot select multiple options!')
        for choice in value:
            option = select.find('option', {'value': choice})
            if not option:
                option = select.find('option', string=choice)
            if not option:
                raise LinkNotFoundError('Option %s not found for select %s' %
                    (choice, name))
            option.attrs['selected'] = 'selected'