def fro(self, statement):
    if not self.name_format:
        return self.fail_safe_fro(statement)
    result = {}
    for attribute in statement.attribute:
        if (attribute.name_format and self.name_format and attribute.
            name_format != self.name_format):
            continue
        try:
            key, val = self.ava_from(attribute)
        except (KeyError, AttributeError):
            pass
        else:
            result[key] = val
    return result