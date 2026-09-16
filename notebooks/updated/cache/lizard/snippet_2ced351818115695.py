def extensions_as_elements(self, tag, schema):
    result = []
    for ext in self.find_extensions(tag, schema.NAMESPACE):
        ets = schema.ELEMENT_FROM_STRING[tag]
        result.append(ets(ext.to_string()))
    return result