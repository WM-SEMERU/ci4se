def to_internal_value(self, data):
    converted_data = _convert_template_id_to_dict(data)
    return super(TemplateSerializer, self).to_internal_value(converted_data)