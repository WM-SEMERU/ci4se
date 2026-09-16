def _gen_indicator_class(self):
    for entry in self.tcex.indicator_types_data.values():
        name = entry.get('name')
        class_name = name.replace(' ', '')
        entry['custom'] = self.tcex.utils.to_bool(entry.get('custom'))
        if class_name in globals():
            continue
        value_fields = []
        if entry.get('value1Label'):
            value_fields.append(entry['value1Label'])
        if entry.get('value2Label'):
            value_fields.append(entry['value2Label'])
        if entry.get('value3Label'):
            value_fields.append(entry['value3Label'])
        value_count = len(value_fields)
        class_data = {}
        custom_class = custom_indicator_class_factory(name, Indicator,
            class_data, value_fields)
        setattr(module, class_name, custom_class)
        self._gen_indicator_method(name, custom_class, value_count)