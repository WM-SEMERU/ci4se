def _get_aria_autocomplete(self, field):
    tag_name = field.get_tag_name()
    input_type = None
    if field.has_attribute('type'):
        input_type = field.get_attribute('type').lower()
    if tag_name == 'TEXTAREA' or tag_name == 'INPUT' and not (input_type ==
        'button' or input_type == 'submit' or input_type == 'reset' or 
        input_type == 'image' or input_type == 'file' or input_type ==
        'checkbox' or input_type == 'radio' or input_type == 'hidden'):
        value = None
        if field.has_attribute('autocomplete'):
            value = field.get_attribute('autocomplete').lower()
        else:
            form = self.parser.find(field).find_ancestors('form').first_result(
                )
            if form is None and field.has_attribute('form'):
                form = self.parser.find('#' + field.get_attribute('form')
                    ).first_result()
            if form is not None and form.has_attribute('autocomplete'):
                value = form.get_attribute('autocomplete').lower()
        if value == 'on':
            return 'both'
        elif field.has_attribute('list') and self.parser.find(
            'datalist[id="' + field.get_attribute('list') + '"]').first_result(
            ) is not None:
            return 'list'
        elif value == 'off':
            return 'none'
    return None