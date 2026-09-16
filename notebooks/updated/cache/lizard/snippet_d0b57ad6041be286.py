def get_value(self, class_name, attr, default_value=None, state='normal',
    base_name='View'):
    styles = self.get_dict_for_class(class_name, state, base_name)
    try:
        return styles[attr]
    except KeyError:
        return default_value