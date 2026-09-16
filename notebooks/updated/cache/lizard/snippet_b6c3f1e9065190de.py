def substitute_xml(cls, value, make_quoted_attribute=False):
    value = cls.AMPERSAND_OR_BRACKET.sub(cls._substitute_xml_entity, value)
    if make_quoted_attribute:
        value = cls.quoted_attribute_value(value)
    return value