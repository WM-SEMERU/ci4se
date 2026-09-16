def CopyFromDict(self, attributes):
    for attribute_name, attribute_value in attributes.items():
        if attribute_name[0] == '_':
            continue
        setattr(self, attribute_name, attribute_value)