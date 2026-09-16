def quoted_attribute_value(self, value):
    quote_with = '"'
    if '"' in value:
        if "'" in value:
            replace_with = '&quot;'
            value = value.replace('"', replace_with)
        else:
            quote_with = "'"
    return quote_with + value + quote_with